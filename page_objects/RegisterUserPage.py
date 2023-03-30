import allure
from selenium.webdriver.common.by import By

from final_project_opencart_autotest.page_objects.BasePage import BasePage


class RegisterUserPage(BasePage):
    FIRST_NAME = (By.ID, "input-firstname")
    LAST_NAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    TELEPHONE = (By.ID, 'input-telephone')
    PASSWORD = (By.ID, "input-password")
    PASSWORD_CONFIRM = (By.ID, "input-confirm")
    PP_CHECK = (By.CSS_SELECTOR, "input[type='checkbox']")
    CONTINUE_BUTTON = (By.CLASS_NAME, "btn.btn-primary")
    FNAME_DANGER_TEXT = (By.XPATH,
                         '//*[text()[contains(., "First Name must be between 1 and 32 characters!")]]')
    LNAME_DANGER_TEXT = (By.XPATH,
                         '//*[text()[contains(., "Last Name must be between 1 and 32 characters!")]]')
    EMAIL_DANGER_TEXT = (By.XPATH,
                         '//*[text()[contains(., "E-Mail Address does not appear to be valid!")]]')
    TELEPHONE_DANGER_TEXT = (By.XPATH,
                             '//*[text()[contains(., "Telephone must be between 3 and 32 characters!")]]')
    PSWD_DANGER_TEXT = (By.XPATH,
                        '//*[text()[contains(., "Password must be between 4 and 20 characters!")]]')
    PSWD_CONFIRM_DANGER_TEXT = (By.XPATH,
                                '//*[text()[contains(., "Password confirmation does not match password!")]]')
    PP_DANGER_TEXT = (By.XPATH,
                      '//*[text()[contains(., " Warning: You must agree to the Privacy Policy!")]]')
    SAME_EMAIL_DANGER_TEXT = (By.XPATH,
                              '//*[text()[contains(., " Warning: E-Mail Address is already registered!")]]')

    @allure.step("I fill mandatory fields for new user")
    def fill_mandatory_fields_for_user(self, f_name, l_name, email, phone, pswd, pswd_conf):
        self._input(self.element(self.FIRST_NAME), f_name)
        self._input(self.element(self.LAST_NAME), l_name)
        self._input(self.element(self.EMAIL), email)
        self._input(self.element(self.TELEPHONE), phone)
        self._input(self.element(self.PASSWORD), pswd)
        self._input(self.element(self.PASSWORD_CONFIRM), pswd_conf)
        return self

    @allure.step("I agree Privacy Policy")
    def agree_pp(self):
        self.click(self.element(self.PP_CHECK))
        return self

    @allure.step("I tap on Continue button")
    def finish_registration(self):
        self.click(self.element(self.CONTINUE_BUTTON))
        return self

    @allure.step("I find info that user is successfully created")
    def success_created_user(self):
        txt = self.driver.find_element(By.CSS_SELECTOR, "div[id='content'].col-sm-9 > h1")
        if txt.text == "Your Account Has Been Created!":
            return self
        else:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Something went wrong. User is not registered")

    @allure.step('I find info that First Name is incorrect')
    def fname_incorrect(self):
        if self.element(self.FNAME_DANGER_TEXT):
            return self
        else:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Something went wrong")

    @allure.step('I find info that Last Name is incorrect')
    def lname_incorrect(self):
        if self.element(self.LNAME_DANGER_TEXT):
            return self
        else:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Something went wrong")

    @allure.step('I find info that Email is incorrect')
    def email_incorrect(self):
        if self.element(self.EMAIL_DANGER_TEXT):
            return self
        else:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Something went wrong")

    @allure.step('I find info that Telephone is incorrect')
    def telephone_incorrect(self):
        if self.element(self.TELEPHONE_DANGER_TEXT):
            return self
        else:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Something went wrong")

    @allure.step('I find info that Password is incorrect')
    def password_incorrect(self):
        if self.element(self.PSWD_DANGER_TEXT):
            return self
        else:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Something went wrong")

    @allure.step('I find info that Password Confirm is incorrect')
    def password_confirm_incorrect(self):
        if self.element(self.PSWD_CONFIRM_DANGER_TEXT):
            return self
        else:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Something went wrong")

    @allure.step('I find info that Privacy Policy should be checked')
    def pp_unchecked(self):
        if self.element(self.PP_DANGER_TEXT):
            return self
        else:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Something went wrong")

    @allure.step('I find info that user should have unique email')
    def email_non_unique(self):
        if self.element(self.SAME_EMAIL_DANGER_TEXT):
            return self
        else:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Something went wrong")

