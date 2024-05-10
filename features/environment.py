from selenium import webdriver
from pages.login_page import LogInPage
from allure_commons.types import AttachmentType as aType
from utils.allure_environment import create_allure_environment

import allure


# Before
def before_all(context):
    print("Opening Driver")

    browser = context.config.userdata.get("browser_name")

    match browser:
        case "Chrome":
            context.driver = webdriver.Chrome()
        case "Firefox":
            context.driver = webdriver.Firefox()

    context.login_page = LogInPage(context.driver)

def before_feature(context, feature):
    pass

def before_tag(context, tag):
    pass

def before_scenario(context, scenario):
    pass

def before_step(context, step):
    pass


# After
def after_all(context):
    print("Quitting driver")
    context.driver.quit()

    path = context.config.userdata.get("os_name") + "_" + context.config.userdata.get("browser_name")
    values = {
        "os_name": context.config.userdata.get("os_name"),
        "browser_name": context.config.userdata.get("browser_name")
    }
    create_allure_environment(path, values)

def after_feature(context, feature):
    pass

def after_tag(context, tag):
    pass

def after_scenario(context, scenario):
    if scenario.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(), name=scenario.name, attachment_type=aType.PNG)

def after_step(context, step):
    pass