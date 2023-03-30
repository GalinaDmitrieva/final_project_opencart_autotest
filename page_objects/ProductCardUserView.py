from selenium.webdriver.common.by import By

from final_project_opencart_autotest.page_objects.BasePage import BasePage


class ProductCardUserView(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "button-cart")
    SHARE_BUTTON = (By.CLASS_NAME, "atc_s.addthis_button_compact")
    QUANTITY_FIELD = (By.ID, "input-quantity")
    COMMON_FIELD_RATING = (By.CLASS_NAME, "rating")
    TABS_PANE = (By.CLASS_NAME, "nav.nav-tabs")

