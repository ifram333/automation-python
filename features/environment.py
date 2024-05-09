from selenium import webdriver
from pages.login_page import LogInPage


# Before
def before_all(context):
    print("Opening Driver")
    context.driver = webdriver.Chrome()
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

def after_feature(context, feature):
    pass

def after_tag(context, tag):
    pass

def after_scenario(context, scenario):
    pass

def after_step(context, step):
    pass