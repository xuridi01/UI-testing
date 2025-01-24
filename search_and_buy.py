from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

#test n.1
@given(u'the user is on the main page')
def step_impl(context):
   context.driver.get("http://opencart:8080/")

@when(u'the user types iMac in the search bar')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("iMac")

@when(u'the user clicks on search icon')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()

@then(u'page with corresponding products appears')
def step_impl(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, ".image .img-fluid")
        assert True

    except NoSuchElementException:
        assert False


#test n.2
@when(u'the user types Huawei nova in the search bar')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("Huawei nova")

@when(u'the user clicks on search')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()

@then(u'page with any product found appears')
def step_impl(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, ".image .img-fluid")
        assert False

    except NoSuchElementException:
        assert True


#test n.3
@when(u'the user clicks on the Desktops button')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Desktops").click()


@when(u'the user clicks on the Mac button')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Mac (1)").click()


@then(u'page with iMac available appears')
def step_impl(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, ".image .img-fluid")
        assert True

    except NoSuchElementException:
        assert False


#test n.4
@given(u'the user is on the page with iMac found')
def step_impl(context):
    context.driver.get("http://opencart:8080/")
    context.driver.find_element(By.LINK_TEXT, "Desktops").click()
    context.driver.find_element(By.LINK_TEXT, "Mac (1)").click()

@when(u'the user clicks on the icon of iMac')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".image .img-fluid").click()

@then(u'page with details about iMac and possibility of adding it into shopping cart appears')
def step_impl(context):
    try:
        context.driver.find_element(By.ID, "button-cart")
        assert True 
    except NoSuchElementException:
        assert False


#test n.5
@given(u'the user is on the page with detailed Samsung SyncMaster 941BW')
def step_impl(context):
    context.driver.get("http://opencart:8080/")
    context.driver.find_element(By.LINK_TEXT, "Components").click()
    context.driver.find_element(By.LINK_TEXT, "Monitors (2)").click()
    context.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(2) > .product-thumb .img-fluid").click()
    

@when(u'the user writes 2 into the Qty bar')
def step_impl(context):
    context.driver.find_element(By.ID, "input-quantity").click()
    time.sleep(3)
    context.driver.find_element(By.ID, "input-quantity").send_keys("2")
    time.sleep(3)

@when(u'the user clicks on the Add to Cart button')
def step_impl(context):
    context.driver.find_element(By.ID, "button-cart").click()
    time.sleep(3)

@then(u'Samsung SyncMaster 941BW monitors are added into the shopping cart')
def step_impl(context):
    alert_element = context.driver.find_element(By.CSS_SELECTOR, ".alert")
    alert_text = alert_element.text
    success_message = alert_text.split(':')[0].strip()
    if(success_message == "Success"):
        assert True
    else:
        assert False


#test n.6
@given(u'the user is on the detailed shopping cart page')
def step_impl(context):
    context.driver.get("http://opencart:8080/")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-inverse").click()
    context.driver.find_element(By.CSS_SELECTOR, ".text-end > a:nth-child(1) > strong").click()

@when(u'the user adds number 1 into the Quantity bar')
def step_impl(context):
    context.driver.find_element(By.NAME, "quantity").click()
    context.driver.find_element(By.NAME, "quantity").send_keys("21")

@when(u'the user clicks on the update button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".fa-rotate").click()
    time.sleep(1)

@then(u'monitors are added into the shoping cart')
def step_impl(context):
    input_element = context.driver.find_element(By.NAME, "quantity")
    input_value = input_element.get_attribute("value")
    int_value = int(input_value)
    if(int_value > 2):
        assert True
    else:
        assert False

@then(u'the price is updated')
def step_impl(context):
    element = context.driver.find_element(By.CSS_SELECTOR, "tbody .text-end:nth-child(6)")
    text_content = element.text
    numeric_value = text_content.replace('$', '')
    numeric_value = numeric_value.split('.')[0].strip()
    numeric_value = numeric_value.replace(',', '')
    numeric_value = int(numeric_value)
    if(numeric_value > 482):
        assert True
    else:
        assert False


#test n.7
@when(u'the user clicks on the checkout button')
def step_impl(context):
    element = context.driver.find_element(By.CSS_SELECTOR, ".col > .btn-primary")
    context.driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, ".col > .btn-primary").click()

@then(u'checkout page appers with bars to fill with billing info')
def step_impl(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "h1")
        assert True
    except:
        assert False


#test n.8
@given(u'the user is on the checkout page')
def step_impl(context):
    context.driver.get("http://opencart:8080/")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-inverse").click()
    context.driver.find_element(By.CSS_SELECTOR, ".text-end > a:nth-child(1) > strong").click()
    element = context.driver.find_element(By.CSS_SELECTOR, ".col > .btn-primary")
    context.driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, ".col > .btn-primary").click()

@when(u'the user fill billing info')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("user")
    context.driver.find_element(By.ID, "input-password").send_keys("bitnami")
    context.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(3) > .col:nth-child(1)").click()
    context.driver.find_element(By.ID, "input-firstname").click()
    context.driver.find_element(By.ID, "input-firstname").send_keys("user")
    context.driver.find_element(By.ID, "input-lastname").click()
    context.driver.find_element(By.ID, "input-lastname").send_keys("UserLast")
    context.driver.find_element(By.ID, "input-email").click()
    context.driver.find_element(By.ID, "input-email").click()
    element = context.driver.find_element(By.ID, "input-email")
    actions = ActionChains(context.driver)
    actions.double_click(element).perform()
    context.driver.find_element(By.ID, "input-email").send_keys("test.user@gmail.com")
    context.driver.find_element(By.ID, "input-shipping-address-1").click()
    context.driver.find_element(By.ID, "input-shipping-address-1").send_keys("Vlkova 1")
    context.driver.find_element(By.ID, "input-shipping-city").click()
    context.driver.find_element(By.ID, "input-shipping-city").send_keys("Brno")
    dropdown = context.driver.find_element(By.ID, "input-shipping-zone")
    dropdown.find_element(By.XPATH, "//option[. = 'Aberdeen']").click()
    context.driver.find_element(By.ID, "button-shipping-methods").click()
    context.driver.find_element(By.ID, "input-shipping-method").send_keys("PPL")
    context.driver.find_element(By.ID, "button-payment-methods").click()
    context.driver.find_element(By.ID, "input-payment-methods").send_keys("Apple pay")

@when(u'the user clicks on the Confirm Order button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#checkout-payment > .text-end").click()


@then(u'the page changes, the order is confirmed and the product should be sent in the future')
def step_impl(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "h1")
        assert False
    except:
        assert True