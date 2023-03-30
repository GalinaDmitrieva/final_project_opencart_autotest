import allure
from selenium.webdriver.common.by import By

from final_project_opencart_autotest.page_objects.BasePage import BasePage


class AdminPage(BasePage):
    ADMIN_USERNAME = (By.ID, "input-username")
    ADMIN_PASSWORD = (By.ID, "input-password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_PSWD_LINK = (By.LINK_TEXT, "Forgotten Password")
    OPENCART_LINK = (By.LINK_TEXT, "OpenCart")

    @allure.step("I log in as admin with {username} and {password}")
    def login(self, username, password):
        self._input(self.element(self.ADMIN_USERNAME), username)
        self._input(self.element(self.ADMIN_PASSWORD), password)
        self.click(self.element(self.LOGIN_BTN))
        return self
