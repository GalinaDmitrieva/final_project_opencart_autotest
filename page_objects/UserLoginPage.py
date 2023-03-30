import time

import allure
from selenium.webdriver.common.by import By

from final_project_opencart_autotest.page_objects.BasePage import BasePage
from final_project_opencart_autotest.page_objects.MainPage import MainPage


class UserLoginPage(BasePage):
    EMAIL_FIELD = (By.ID, "input-email")
    PSWD_FIELD = (By.ID, 'input-password')
    USER_LOGIN_BTN = (By.CSS_SELECTOR, "input[type='submit']")
    INFO_INCORRECT_CREDENTIALS = (By.XPATH,
                                  '//*[text()[contains(., " Warning: No match for E-Mail Address and/or Password.")]]')
    INFO_TOO_MUCH_INCORRECT_LOGIN = (By.XPATH,
                                     '//*[text()[contains(., " Warning: Your account has exceeded allowed number of '
                                     'login attempts. Please try again in 1 hour.")]]')

    @allure.step("I log in as user with {email} and {password}")
    def authorize_by_user(self, email, password):
        self._input(self.element(self.EMAIL_FIELD), email)
        self._input(self.element(self.PSWD_FIELD), password)
        self.click(self.element(self.USER_LOGIN_BTN))
        return self

    @allure.step("I find info if authorization is failed when incorrect credentials")
    def if_authorization_incorrect(self):
        if self.element(self.INFO_INCORRECT_CREDENTIALS):
            return self
        else:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Something went wrong")

    @allure.step("I find info if too much attempts with incorrect credentials")
    def if_too_much_attempts(self):
        if self.element(self.INFO_TOO_MUCH_INCORRECT_LOGIN):
            return self
        else:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Something went wrong")
