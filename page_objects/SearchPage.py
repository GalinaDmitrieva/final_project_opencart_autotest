import time

import allure
from selenium.webdriver.common.by import By

from final_project_opencart_autotest.page_objects.BasePage import BasePage


class SearchPage(BasePage):
    SEARCH_FIELD = (By.ID, "input-search")
    SEARCH_BUTTON = (By.ID, "button-search")
    INFO_EMPTY_SEARCH = (By.XPATH,
                         '//*[text()[contains(., "There is no product that matches the search criteria.")]]')

    @allure.step("I perform search on Search page")
    def enter_search_request(self, req_text):
        self._input(self.element(self.SEARCH_FIELD), req_text)
        self.click(self.element(self.SEARCH_BUTTON))
        return self

    @allure.step("I find if element with certain name is presented on Search page with results")
    def find_required_product(self, prod_name):
        self.element((By.PARTIAL_LINK_TEXT, prod_name))
        return self

    @allure.step("I find info if search result is empty")
    def empty_search(self):
        self.element(self.INFO_EMPTY_SEARCH)
        return self

