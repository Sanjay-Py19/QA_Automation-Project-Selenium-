from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.loginPage import LoginPage


@given(u'login with valid credentials')
def userPass(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.userName("Newman")
    context.login_page.passWord("Newman")


@when(u'Provide valid user and password')
def loginButton(context):
    context.login_button = LoginPage(context.driver)
    context.login_button.clickLogin()


@then(u'Login to system')
def loggedIn(context):
    try:
        status = context.driver.find_element(By.XPATH, "//*[normalize-space()='Welcome Newman Great']")
        assert status is not None  # Assert that the element is found
    except:
        assert False, "Element with text 'Welcome Newman Great' not found"
    finally:
        context.driver.quit()
