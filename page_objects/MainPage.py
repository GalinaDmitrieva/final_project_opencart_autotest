import time

import allure
from selenium.webdriver.common.by import By

from final_project_opencart_autotest.page_objects.BasePage import BasePage


class MainPage(BasePage):
    ACCOUNT_MENU = (By.CSS_SELECTOR, "li.dropdown > a")
    REGISTER_OPTION = (By.LINK_TEXT, "Register")
    LOGIN_OPTION = (By.LINK_TEXT, "Login")
    LOGOUT_OPTION = (By.LINK_TEXT, "Logout")
    CURRENCY_MENU = (By.ID, "form-currency")
    EUR_OPTION = (By.XPATH, "//button[text()='€ Euro']")
    GBR_OPTION = (By.XPATH, "//button[text()='£ Pound Sterling']")
    USD_OPTION = (By.XPATH, "//button[text()='$ US Dollar']")
    LOGO = (By.ID, "logo")
    SEARCH_FIELD = (By.ID, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='button'].btn.btn-default.btn-lg")
    NON_EXISTED_ELEM = (By.ID, "non-existed-elem")
    CART_LIST = (By.ID, "cart")

    @allure.step("I open Account menu")
    def open_account_menu(self):
        self.click(self.element(self.ACCOUNT_MENU))
        return self

    @allure.step("I open Register form")
    def open_register_form(self):
        self.click(self.element(self.REGISTER_OPTION))
        return self

    @allure.step("I open Currency menu")
    def open_currency_menu(self):
        self.click(self.element(self.CURRENCY_MENU))
        return self

    @allure.step("I change currency and check if it is correctly set")
    def change_currency(self, currency):
        if currency == "EUR":
            self.click(self.element(self.EUR_OPTION))
            with allure.step("I check that currency is correctly set"):
                if self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-link.dropdown-toggle > strong") == '€':
                    return self
                else:
                    return AssertionError("Something went wrong")
        elif currency == "GBR":
            self.click(self.element(self.GBR_OPTION))
            with allure.step("I check that currency is correctly set"):
                if self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-link.dropdown-toggle > strong") == '£':
                    return self
                else:
                    return AssertionError("Something went wrong")
        elif currency == "USD":
            self.click(self.element(self.USD_OPTION))
            with allure.step("I check that currency is correctly set"):
                if self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-link.dropdown-toggle > strong") == '$':
                    return self
                else:
                    return AssertionError("Something went wrong")
        else:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("No such currency")

    @allure.step("I open Search page")
    def open_search_page(self):
        self.click(self.element(self.SEARCH_BUTTON))
        return self

    @allure.step('I open Login page for customer')
    def open_login_page(self):
        self.click(self.element(self.LOGIN_OPTION))
        return self

    @allure.step('I find Logout option for authorized user')
    def is_logout_option_present(self):
        if self.element(self.LOGOUT_OPTION):
            return self
        else:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Something went wrong")



