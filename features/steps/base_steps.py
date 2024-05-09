from behave import *
from assertpy import *


@given('The page loads')
def step_impl(context):
    context.driver.get('https://www.saucedemo.com/')
    assert_that(context.driver.title).is_equal_to("Swag Labs")
    