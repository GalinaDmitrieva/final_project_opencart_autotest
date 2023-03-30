import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Clicking element: {element}")
    def click(self, element):
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    @allure.step("Clicking element: {element}")
    def _input(self, element, value):
        self.click(element)
        element.clear()
        element.send_keys(value)

    @allure.step("Check if element {locator} is present")
    def element(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f"Not wait element {locator}")
