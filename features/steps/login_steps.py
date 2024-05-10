from behave import *
from assertpy import fail
import time


@given('The user enters the "{username}" and "{password}"')
def step_impl(context, username, password):
    context.login_page.fillUsername(username)
    context.login_page.fillPassword(password)

@when('The user clicks on the log in button')
def step_impl(context):
    context.login_page.clickLogIn()

@then('The user is logged in successfully')
def step_impl(context):
    time.sleep(5)
    pass
    
