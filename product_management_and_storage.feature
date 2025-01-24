Feature: Product management and product storage

    Background:
        Given the user is logged in as administrator John Doe

    Scenario: List all products n.9
        Given the admin is on the home admin page
        When the admin clicks on Catalog in the side nav bars
        And clicks on the Products button
        Then page with all listed products appears

    Scenario: Add new product n.10
        Given the admin is on the page with listed products
        When the admin clicks on the Add New button
        And the admin fills information about new product
        And the admin clicks on Save button
        Then new product appears on the Products page

    Scenario: Delete product n.11
        Given the admin is on the page with listed products with his desired product
        When the admin marks product on the left side of the product in check box
        And the admin clicks on the Delete button
        Then this product dont appears on the filtred Products page

    Scenario: Change product status n.12
        Given the admin is on the page with listed products
        When the admin clicks on the Edit product button of Canon EOS 5D 
        And the admin clicks on the Data button in the upper navbar
        And the admin change status on disabled and do save
        Then the product is disabled on the Products page

    Scenario: Change product quantity n.13 
        Given the admin is on the page with listed products
        When the admin clicks on the Edit product button of HP LP3065
        And the admin clicks on the Data button in the upper navbar
        And the admin change quantity on 0
        Then the product appears with 0 quantity

    Scenario: Change product name and description n.14
        Given the admin is on the page with listed products
        When the admin clicks on the Edit product button of Canon EOS 5D
        And the admin changes the product name on Test_product
        Then the product appears on the Products page as Test_product

