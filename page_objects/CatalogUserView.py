from selenium.webdriver.common.by import By

from final_project_opencart_autotest.page_objects.BasePage import BasePage


class CatalogUserView(BasePage):
    NAVIGATION_PANE = (By.ID, "column-left")
    DEFAULT_VIEW_OPTION = (By.CSS_SELECTOR, "button[type='button'].btn.btn-default")
    SORT_LIST = (By.ID, "input-sort")
    LIST_VIEW_OPTION = (By.ID, "list-view")
    GRID_VIEW_OPTION = (By.ID, "grid-view")
    NON_EXISTED_ELEM = (By.CSS_SELECTOR, "non_existed_elem")

