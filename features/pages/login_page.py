from seleniumpagefactory.Pagefactory import PageFactory

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s.%(msecs)03d %(levelname)s %(name)s.%(funcName)s :: %(message)s',
                    datefmt='%H:%M:%S')


class LogInPage(PageFactory):

    locators = {
        "usernameInput": ('ID', 'user-name'),
        "passwordInput": ('XPATH', '//*[@id="password"]'),
        "logInButton": ('NAME', 'login-button')
    }

    def __init__(self, driver):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.driver = driver
        self.timeout = 30

    def fillUsername(self, username):
        self.usernameInput.set_text(username)
        self.logger.info(f"Fill the username: <{username}>")

    def fillPassword(self, password):
        self.passwordInput.set_text(password)
        self.logger.info(f"Fill the password: <{password}>")

    def clickLogIn(self):
        self.logInButton.click_button()
        self.logger.info(f"Click the log in button")