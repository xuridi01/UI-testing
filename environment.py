#!/usr/bin/env python3
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


def get_driver():
    '''Get Chrome/Firefox driver from Selenium Hub'''
    try:
        driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                #desired_capabilities=DesiredCapabilities.FIREFOX)
                options=webdriver.ChromeOptions())
        
    except WebDriverException:
        driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                #desired_capabilities=DesiredCapabilities.CHROME)
                options=webdriver.FirefoxOptions())
        
    driver.implicitly_wait(5)
    return driver

def before_all(context):
    context.driver = get_driver()

def after_all(context):
    if context.driver:
        context.driver.quit()






        # Copyright VMware, Inc.
# SPDX-License-Identifier: APACHE-2.0

# version: '2'
# services:
#   mariadb:
#     image: docker.io/bitnami/mariadb:11.3
#     environment:
#       # ALLOW_EMPTY_PASSWORD is recommended only for development.
#       - ALLOW_EMPTY_PASSWORD=yes
#       - MARIADB_USER=bn_opencart
#       - MARIADB_DATABASE=bitnami_opencart
#     volumes:
#       - 'mariadb_data:/bitnami/mariadb'
#   opencart:
#     image: docker.io/bitnami/opencart:4
#     ports:
#       - '80:8080'
#       - '443:8443'
#     environment:
#       - OPENCART_HOST=localhost
#       - OPENCART_DATABASE_HOST=mariadb
#       - OPENCART_DATABASE_PORT_NUMBER=3306
#       - OPENCART_DATABASE_USER=bn_opencart
#       - OPENCART_DATABASE_NAME=bitnami_opencart
#       # ALLOW_EMPTY_PASSWORD is recommended only for development.
#       - ALLOW_EMPTY_PASSWORD=yes
#     volumes:
#       - 'opencart_data:/bitnami/opencart'
#       - 'opencart_storage_data:/bitnami/opencart_storage/'
#     depends_on:
#       - mariadb
# volumes:
#   mariadb_data:
#     driver: local
#   opencart_data:
#     driver: local
#   opencart_storage_data:
#     driver: local