import allure
from selenium.webdriver.common.by import By

from final_project_opencart_autotest.page_objects.BasePage import BasePage


class ProductCardAdminView(BasePage):
    PRODUCT_NAME = (By.ID, "input-name1")
    META_TAG_TITLE = (By.ID, "input-meta-title1")
    MODEL = (By.ID, "input-model")
    TAB_GENERAL = (By.LINK_TEXT, "General")
    TAB_DATA = (By.LINK_TEXT, "Data")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit'].btn.btn-primary")
    FILTER_BUTTON = (By.CSS_SELECTOR, "button[type='button'].btn.btn-default.hidden-md.hidden-lg")
    FILTER_PROD_NAME = (By.ID, "input-name")
    APPLY_FILTER_BUTTON = (By.ID, "button-filter")

    @allure.step("I fill new product form with product name {product_name}, "
                 "meta tag title {meta_tag_title}, "
                 "model {model}")
    def fill_mandatory_fields(self, product_name, meta_tag_title, model):
        self._input(self.element(self.PRODUCT_NAME), product_name)
        self._input(self.element(self.META_TAG_TITLE), meta_tag_title)
        self.click(self.element(self.TAB_DATA))
        self._input(self.element(self.MODEL), model)
        return self

    @allure.step('I save new product')
    def save_product(self):
        self.click(self.element(self.SAVE_BUTTON))
        return self

    def press_filter(self):
        self.click(self.element(self.FILTER_BUTTON))
        return self

    def fill_filter_form(self, product_name):
        self._input(self.element(self.FILTER_PROD_NAME), product_name)
        self.click(self.element(self.APPLY_FILTER_BUTTON))
        return self

    def num_pages_of_table(self):
        num_pages = 1
        elem = self.element((By.CLASS_NAME, "col-sm-6.text-right"))
        txt = elem.text
        num_pages = int(txt[txt.find("(") + 1])
        return num_pages

    def num_elements_of_table(self):
        num_elem = 0
        elem = self.element((By.CLASS_NAME, "col-sm-6.text-right"))
        txt = elem.text
        num_elem = int(txt[txt.find("(") - 3] + txt[txt.find("(") - 2])
        return num_elem

    def find_product_in_list_by_name(self, product_name):
        # находим кол-во страниц таблицы
        num_pages = self.num_pages_of_table()
        i = 1
        checkbox_element = None
        # проходим по всем страницам
        while i <= num_pages:
            # time.sleep(2)
            # получаем таблицу с текущей страницы
            table = self.element((By.TAG_NAME, 'tbody'))
            # получаем список всех строк на текущей странице
            tr = table.find_elements(By.TAG_NAME, "tr")
            j = 0
            # проходим по строкам таблицы
            while j <= (len(tr) - 1):
                # узнаем имя продукта которое указано в текущей строке
                product_value = tr[j].find_elements(By.CLASS_NAME, "text-left")[0].text
                # если имя продукта соответствует тому которое указано
                if product_value == product_name:
                    # находим элемент чекбокса для текущей строки
                    checkbox_element = tr[j].find_element(By.CSS_SELECTOR, "input[type='checkbox']")
                    break
                # если имя продукта не соответствует переходим к следующей строке
                else:
                    j = j + 1
            if checkbox_element != None:
                break
            # если кол-во страниц больше одной переключаемся на следующую страницу
            i = i + 1
            if i <= num_pages:
                self.click(self.element((By.LINK_TEXT, str(i))))
            else:
                break

        if checkbox_element is not None:
            return checkbox_element
        else:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("No such product")

    def remove_product_from_list_by_name(self, product_name):
        element = self.find_product_in_list_by_name(product_name)
        if element is not None:
            element.click()
            delBtn = self.element((By.CSS_SELECTOR, "button[type='button'].btn.btn-danger"))
            delBtn.click()
            al_obj = self.driver.switch_to.alert
            al_obj.accept()
        else:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Impossible to remove the product")
