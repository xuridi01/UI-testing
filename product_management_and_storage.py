from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given(u'the user is logged in as administrator John Doe')
def step_impl(context):
    time.sleep(1)
    context.driver.get("http://opencart:8080/administration/")
    context.driver.find_element(By.ID, "input-username").click()
    context.driver.find_element(By.ID, "input-username").send_keys("user")
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("bitnami")
    context.driver.find_element(By.CSS_SELECTOR, ".btn").click()


#test n.9
@given(u'the admin is on the home admin page')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "h1")

@when(u'the admin clicks on Catalog in the side nav bars')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Catalog").click()

@when(u'clicks on the Products button')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Products").click()

@then(u'page with all listed products appears')
def step_impl(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "h1")
        assert True
    except:
        assert False


#test n.10
@given(u'the admin is on the page with listed products')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Catalog").click()
    context.driver.find_element(By.LINK_TEXT, "Products").click()

@when(u'the admin clicks on the Add New button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn > .fa-plus").click()

@when(u'the admin fills information about new product')
def step_impl(context):
    context.driver.find_element(By.ID, "input-name-1").click()
    context.driver.find_element(By.ID, "input-name-1").send_keys("product")
    context.driver.find_element(By.ID, "input-meta-title-1").click()
    context.driver.find_element(By.ID, "input-meta-title-1").send_keys("1")
    context.driver.find_element(By.LINK_TEXT, "Data").click()
    context.driver.find_element(By.ID, "input-model").click()
    context.driver.find_element(By.ID, "input-model").send_keys("model")
    context.driver.find_element(By.LINK_TEXT, "SEO").click()
    context.driver.find_element(By.ID, "input-keyword-0-1").click()
    context.driver.find_element(By.ID, "input-keyword-0-1").send_keys("key")

@when(u'the admin clicks on Save button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".float-end > .btn-primary").click()

@then(u'new product appears on the Products page')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Products").click()
    context.driver.find_element(By.ID, "input-model").click()
    context.driver.find_element(By.ID, "input-model").send_keys("model")
    context.driver.find_element(By.ID, "button-filter").click()
    try:
        context.driver.find_element(By.CSS_SELECTOR, "tbody > tr:nth-child(1) > .d-none")
        assert True
    except:
        assert False


#test n.11
@given(u'the admin is on the page with listed products with his desired product')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Catalog").click()
    context.driver.find_element(By.LINK_TEXT, "Products").click()
    context.driver.find_element(By.LINK_TEXT, "Products").click()
    context.driver.find_element(By.ID, "input-model").click()
    context.driver.find_element(By.ID, "input-model").send_keys("model")
    context.driver.find_element(By.ID, "button-filter").click()

@when(u'the admin marks product on the left side of the product in check box')
def step_impl(context):
    element = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "selected[]"))
    )
    element.click()

@when(u'the admin clicks on the Delete button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn-danger").click()
    assert context.driver.switch_to.alert.text == "Are you sure?"
    context.driver.switch_to.alert.accept()

@then(u'this product dont appears on the filtred Products page')
def step_impl(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "tbody > tr:nth-child(1) > .d-none")
        assert False
    except:
        assert True


#test n.12
@when(u'the admin clicks on the Edit product button of Canon EOS 5D')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) .fa-pencil").click()

@when(u'the admin clicks on the Data button in the upper navbar')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Data").click()

@when(u'the admin change status on disabled and do save')
def step_impl(context):
    element = context.driver.find_element(By.ID, "input-status")
    context.driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(1)
    context.driver.find_element(By.ID, "input-status").click()

    element = context.driver.find_element(By.CSS_SELECTOR, ".float-end > .btn-primary")
    context.driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, ".float-end > .btn-primary").click()

@then(u'the product is disabled on the Products page')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Products").click()
    element = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-danger:nth-child(2)"))
    )
    text = element.text
    text = text.strip()
    if(text == "Disabled"):
        assert True
    else:
        assert False


#test n.13 
@when(u'the admin clicks on the Edit product button of HP LP3065')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) .btn:nth-child(1)").click()

@when(u'the admin change quantity on 0')
def step_impl(context):
    element = context.driver.find_element(By.ID, "input-quantity")
    context.driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(1)
    context.driver.find_element(By.ID, "input-quantity").clear()
    context.driver.find_element(By.ID, "input-quantity").click()
    context.driver.find_element(By.ID, "input-quantity").send_keys("0")

    element = context.driver.find_element(By.CSS_SELECTOR, ".float-end > .btn-primary")
    context.driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, ".float-end > .btn-primary").click()

@then(u'the product appears with 0 quantity')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Products").click()
    element = context.driver.find_element(By.CSS_SELECTOR, ".text-end > .bg-warning")
    text = element.text
    text = text.strip()
    text = int(text)
    
    if(text == 0):
        assert True
    else:
        assert False

#test n.14 
@when(u'the admin changes the product name on Test_product')
def step_impl(context):
    context.driver.find_element(By.ID, "input-name-1").clear()
    context.driver.find_element(By.ID, "input-name-1").click()
    context.driver.find_element(By.ID, "input-name-1").send_keys("Test_product")
    context.driver.find_element(By.CSS_SELECTOR, ".fa-floppy-disk").click()

@then(u'the product appears on the Products page as Test_product')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Products").click()
    context.driver.find_element(By.ID, "input-name").click()
    context.driver.find_element(By.ID, "input-name").send_keys("Test_product")
    context.driver.find_element(By.ID, "button-filter").click()
    element = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "tbody .text-start:nth-child(3)"))
    )
    text = element.text.strip()
    part_text = text.split()[0]
    if(part_text == "Test_product"):
        assert True
    else:
        assert False