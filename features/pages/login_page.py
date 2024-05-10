from features.pages.base_page import BasePage

import logging


class LogInPage(BasePage):

    locators = {
        "usernameInput": ('ID', 'user-name'),
        "passwordInput": ('XPATH', '//*[@id="password"]'),
        "logInButton": ('NAME', 'login-button')
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(self.__class__.__name__)

    def fillUsername(self, username):
        self.usernameInput.set_text(username)
        self.logger.info(f"Fill the username: <{username}>")

    def fillPassword(self, password):
        self.passwordInput.set_text(password)
        self.logger.info(f"Fill the password: <{password}>")

    def clickLogIn(self):
        self.logInButton.click_button()
        self.logger.info(f"Click the log in button")