Feature: Search and buy products

    Scenario: Search for the available desired product n.1
        Given the user is on the main page
        When the user types iMac in the search bar
        And the user clicks on search icon
        Then page with corresponding products appears

    Scenario: Search for the not available desired product n.2
        Given the user is on the main page
        When the user types Huawei nova in the search bar
        And the user clicks on search
        Then page with any product found appears

    Scenario: List products by category n.3
        Given the user is on the main page
        When the user clicks on the Desktops button
        And the user clicks on the Mac button 
        Then page with iMac available appears

    Scenario: Show desired product detailed n.4
        Given the user is on the page with iMac found
        When the user clicks on the icon of iMac
        Then page with details about iMac and possibility of adding it into shopping cart appears

    Scenario: Add product to the shopping cart n.5
        Given the user is on the page with detailed Samsung SyncMaster 941BW
        When the user writes 2 into the Qty bar
        And the user clicks on the Add to Cart button
        Then Samsung SyncMaster 941BW monitors are added into the shopping cart

    Scenario: Updating number of products in the shopping cart n.6
        Given the user is on the detailed shopping cart page 
        When the user adds number 1 into the Quantity bar
        And the user clicks on the update button
        Then monitors are added into the shoping cart
        And the price is updated

    Scenario: Going on the checkout page n.7
        Given the user is on the detailed shopping cart page
        When the user clicks on the checkout button
        Then checkout page appers with bars to fill with billing info

    Scenario: Billing info and confirming order n.8
        Given the user is on the checkout page
        When the user fill billing info:
            | First Name | Last Name | E-mail              | Address 1 | City | Post Code | Region/State | Shipping Method | Payment Method |
            | user       | userLast  | test.user@gamil.com | Vlkova 1  | Brno | 628 00    | Aberdeen     | PPL             | ApplePay       |
        And the user clicks on the Confirm Order button
        Then the page changes, the order is confirmed and the product should be sent in the future
