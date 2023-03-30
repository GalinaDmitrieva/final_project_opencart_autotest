import allure
from selenium.webdriver.common.by import By

from final_project_opencart_autotest.page_objects.BasePage import BasePage


class AdminHomePage(BasePage):
    CATALOG_MENU = (By.LINK_TEXT, "Catalog")
    PRODUCTS_OPTION = (By.LINK_TEXT, "Products")
    ADD_BUTTON = (By.CLASS_NAME, "btn.btn-primary")
    CUSTOMERS_MENU = (By.PARTIAL_LINK_TEXT, "Customers")
    CUSTOMERS_OPTION = (By.XPATH, '//a[contains(@href,"customer")]')
    SELECT_ALL_CUSTOMERS = (By.CSS_SELECTOR, "input[onclick*='$(']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button[type='button'].btn.btn-danger")
    MODIFIED_CUSTOMERS_INFO_TEXT = (By.XPATH,
                                    '//*[text()[contains(., " Success: You have modified customers!")]]')
    EMPTY_TABLE_INFO = (By.XPATH, '//*[text()[contains(., "No results!")]]')

    @allure.step("I open Catalog menu")
    def open_catalog_menu(self):
        self.click(self.element(self.CATALOG_MENU))
        return self

    @allure.step("I open Product list page")
    def open_product_list(self):
        self.click(self.element(self.PRODUCTS_OPTION))
        return self

    @allure.step("I open new product form")
    def open_product_form(self):
        self.click(self.element(self.ADD_BUTTON))
        return self

    @allure.step("I open Customers menu")
    def open_customers_menu(self):
        self.click(self.element(self.CUSTOMERS_MENU))
        return self

    @allure.step("I open Customers list")
    def open_customers_list(self):
        self.click(self.element(self.CUSTOMERS_OPTION))
        return self

    @allure.step("I select all customers in list")
    def select_all_customers(self):
        self.click(self.element(self.SELECT_ALL_CUSTOMERS))
        return self

    @allure.step("I delete all customers in list")
    def confirmed_deletion(self):
        self.click(self.element(self.DELETE_BUTTON))
        obj = self.driver.switch_to.alert
        obj.accept()
        return self

    @allure.step("I find modification customers info")
    def is_modification_info(self):
        if self.element(self.MODIFIED_CUSTOMERS_INFO_TEXT):
            return self
        else:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Something went wrong")

    @allure.step("I find modification customers info")
    def is_table_empty(self):
        if self.element(self.EMPTY_TABLE_INFO):
            return self
        else:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Something went wrong")

