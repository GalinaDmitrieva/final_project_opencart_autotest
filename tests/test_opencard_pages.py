import time

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from final_project_opencart_autotest.page_objects.AdminHomePage import AdminHomePage
from final_project_opencart_autotest.page_objects.AdminPage import AdminPage
from final_project_opencart_autotest.page_objects.CatalogUserView import CatalogUserView
from final_project_opencart_autotest.page_objects.MainPage import MainPage
from final_project_opencart_autotest.page_objects.SearchPage import SearchPage
from final_project_opencart_autotest.page_objects.UserLoginPage import UserLoginPage
from final_project_opencart_autotest.page_objects.ProductCardAdminView import ProductCardAdminView
from final_project_opencart_autotest.page_objects.ProductCardUserView import ProductCardUserView
from final_project_opencart_autotest.page_objects.RegisterUserPage import RegisterUserPage


@allure.title("Check some existed elements on main page")
def test_existed_elem_main_page(browser, url):
    """Check some elements on main page"""
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser).element(MainPage(browser).LOGO)
    MainPage(browser).element(MainPage(browser).SEARCH_FIELD)
    MainPage(browser).element(MainPage(browser).SEARCH_BUTTON)
    MainPage(browser).element(MainPage(browser).CURRENCY_MENU)
    MainPage(browser).element(MainPage(browser).CART_LIST)
    time.sleep(10)


@allure.title("Check some existed elements on Catalog page for user")
def test_existed_elem_catalog(browser, url):
    """Check some elements on Catalog page for user"""
    browser.get(f'{url}/desktops')
    wait = WebDriverWait(browser, 5)
    CatalogUserView(browser).element(CatalogUserView(browser).NAVIGATION_PANE)
    CatalogUserView(browser).element(CatalogUserView(browser).DEFAULT_VIEW_OPTION)
    CatalogUserView(browser).element(CatalogUserView(browser).SORT_LIST)
    CatalogUserView(browser).element(CatalogUserView(browser).LIST_VIEW_OPTION)
    CatalogUserView(browser).element(CatalogUserView(browser).GRID_VIEW_OPTION)


@allure.title("Check some existed elements on Product card page for user")
def test_existed_elem_card(browser, url):
    """Check some elements on Product card page for user"""
    browser.get(f'{url}/desktops/htc-touch-hd?sort=p.sort_order&order=ASC')
    wait = WebDriverWait(browser, 5)
    ProductCardUserView(browser).element(ProductCardUserView(browser).ADD_TO_CART_BUTTON)
    ProductCardUserView(browser).element(ProductCardUserView(browser).SHARE_BUTTON)
    ProductCardUserView(browser).element(ProductCardUserView(browser).QUANTITY_FIELD)
    ProductCardUserView(browser).element(ProductCardUserView(browser).COMMON_FIELD_RATING)
    ProductCardUserView(browser).element(ProductCardUserView(browser).TABS_PANE)


@allure.title("Check some existed elements on admin authorization page ")
def test_existed_elem_admin_page(browser, url):
    """ Check some elements on admin authorization page """
    browser.get(f'{url}/admin')
    wait = WebDriverWait(browser, 5)
    AdminPage(browser).element(AdminPage(browser).ADMIN_USERNAME)
    AdminPage(browser).element(AdminPage(browser).ADMIN_PASSWORD)
    AdminPage(browser).element(AdminPage(browser).FORGOTTEN_PSWD_LINK)
    AdminPage(browser).element(AdminPage(browser).LOGIN_BTN)
    AdminPage(browser).element(AdminPage(browser).OPENCART_LINK)


@allure.title("Check some existed elements on user creation page")
def test_existed_elem_create_user_page(browser, url):
    """Check some elements on user creation page"""
    browser.get(f'{url}/index.php?route=account/register')
    wait = WebDriverWait(browser, 5)
    RegisterUserPage(browser).element(RegisterUserPage(browser).FIRST_NAME)
    RegisterUserPage(browser).element(RegisterUserPage(browser).LAST_NAME)
    RegisterUserPage(browser).element(RegisterUserPage(browser).EMAIL)
    RegisterUserPage(browser).element(RegisterUserPage(browser).PASSWORD)
    RegisterUserPage(browser).element(RegisterUserPage(browser).CONTINUE_BUTTON)


@allure.title("Check successful addition a product in product list")
def test_add_product_to_list(browser, url):
    """Check successful addition a product in product list"""
    prod_name = 'test_product_123'
    meta_tags = 'meta_tags_123'
    model = 'model123'

    browser.get(f'{url}/admin')
    wait = WebDriverWait(browser, 5)
    AdminPage(browser). \
        login(username='user', password='bitnami')

    AdminHomePage(browser). \
        open_catalog_menu(). \
        open_product_list(). \
        open_product_form()

    ProductCardAdminView(browser). \
        fill_mandatory_fields(product_name=prod_name, meta_tag_title=meta_tags, model=model). \
        save_product()

    AdminHomePage(browser). \
        open_product_list()

    ProductCardAdminView(browser). \
        find_product_in_list_by_name(product_name=prod_name)


@allure.title("Creation of new user with valid credentials")
def test_create_new_valid_user(browser, url):
    """Check creation a valid user"""
    f_name = "test"
    l_name = "test"
    email = "test4@tt.ru"
    phone = "1231231"
    pswd = "qwerty"
    pswd_conf = "qwerty"

    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser). \
        open_account_menu(). \
        open_register_form()
    RegisterUserPage(browser). \
        fill_mandatory_fields_for_user(f_name=f_name,
                                       l_name=l_name,
                                       email=email,
                                       phone=phone,
                                       pswd=pswd,
                                       pswd_conf=pswd_conf). \
        agree_pp(). \
        finish_registration(). \
        success_created_user()


@allure.title("Check that impossible to register user with non-unique email and error is displayed")
def test_create_new_user_with_non_unique_email(browser, url):
    """Check that impossible to register user with non-unique email and error is displayed"""
    f_name = "test"
    l_name = "test"
    email = "test4@tt.ru"
    phone = "1231231"
    pswd = "qwerty"
    pswd_conf = "qwerty"

    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser). \
        open_account_menu(). \
        open_register_form()
    RegisterUserPage(browser). \
        fill_mandatory_fields_for_user(f_name=f_name,
                                       l_name=l_name,
                                       email=email,
                                       phone=phone,
                                       pswd=pswd,
                                       pswd_conf=pswd_conf). \
        agree_pp(). \
        finish_registration(). \
        email_non_unique()


@allure.title("Check currency changing on main page to valid one")
@pytest.mark.parametrize('currency', ['EUR', 'USD', 'GBR'])
def test_valid_change_currency(browser, url, currency):
    """Check currency changing on main page to valid one"""
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser).open_currency_menu().change_currency(currency=currency)


@allure.title("Check some existed elements on search page")
def test_existed_elem_search_page(browser, url):
    """Check some elements on search page"""
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser).open_search_page()
    SearchPage(browser).element(SearchPage(browser).SEARCH_FIELD)
    SearchPage(browser).element(SearchPage(browser).SEARCH_BUTTON)


@allure.title("Check not empty search request by {req} on Search page")
@pytest.mark.parametrize('req', ['Canon', 'MacBook', 'HP', 'HTC', 'iPhone', 'iPod', 'Palm', 'Samsung', 'Sony'])
def test_not_empty_search(browser, url, req):
    """Check not empty search result on Search page"""
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser).open_search_page()
    SearchPage(browser).enter_search_request(req).find_required_product(req)


@allure.title("Check empty search request by {req} on Search page")
@pytest.mark.parametrize('req', ['0000', 'Canоn', 'qweqweqwe'])
def test_empty_search(browser, url, req):
    """Check empty search result on Search page"""
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser).open_search_page()
    SearchPage(browser).enter_search_request(req).empty_search()


@allure.title("Check user authorization with correct credentials")
def test_authorization_with_correct_email(browser, url):
    """Check user authorization with correct credentials"""
    em = 'test4@tt.ru'
    psw = 'qwerty'
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser).open_account_menu().open_login_page()
    UserLoginPage(browser).authorize_by_user(email=em, password=psw)
    MainPage(browser).open_account_menu().is_logout_option_present()


@allure.description('REQUIREMENTS - First Name must be between 1 and 32 characters')
@allure.title("Check that impossible to register user with incorrect First Name {inv_fname} and error is displayed")
@pytest.mark.parametrize('inv_fname', ['', 'test11111111111111111111111111111', ' '])
def test_register_with_incorrect_fname(browser, url, inv_fname):
    """Check that impossible to register user with incorrect First Name and error is displayed"""
    l_name = "test"
    email = "test4@tt.ru"
    phone = "1231231"
    pswd = "qwerty"
    pswd_conf = "qwerty"
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser). \
        open_account_menu(). \
        open_register_form()
    RegisterUserPage(browser). \
        fill_mandatory_fields_for_user(f_name=inv_fname,
                                       l_name=l_name,
                                       email=email,
                                       phone=phone,
                                       pswd=pswd,
                                       pswd_conf=pswd_conf). \
        agree_pp(). \
        finish_registration(). \
        fname_incorrect()


@allure.description('REQUIREMENTS - Last Name must be between 1 and 32 characters')
@allure.title("Check that impossible to register user with incorrect Last Name {inv_lname} and error is displayed")
@pytest.mark.parametrize('inv_lname', ['', 'test11111111111111111111111111112', ' '])
def test_register_with_incorrect_lname(browser, url, inv_lname):
    """Check that impossible to register user with incorrect Last Name and error is displayed"""
    f_name = "test"
    email = "test4@tt.ru"
    phone = "1231231"
    pswd = "qwerty"
    pswd_conf = "qwerty"
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser). \
        open_account_menu(). \
        open_register_form()
    RegisterUserPage(browser). \
        fill_mandatory_fields_for_user(f_name=f_name,
                                       l_name=inv_lname,
                                       email=email,
                                       phone=phone,
                                       pswd=pswd,
                                       pswd_conf=pswd_conf). \
        agree_pp(). \
        finish_registration(). \
        lname_incorrect()


@allure.title("Check that impossible to register user with incorrect Email {inv_email} and error is displayed")
@pytest.mark.parametrize('inv_email', ['', '123@123.123', ' '])
def test_register_with_incorrect_email(browser, url, inv_email):
    """Check that impossible to register user with incorrect Email and error is displayed"""
    l_name = 'test'
    f_name = "test"
    phone = "1231231"
    pswd = "qwerty"
    pswd_conf = "qwerty"
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser). \
        open_account_menu(). \
        open_register_form()
    RegisterUserPage(browser). \
        fill_mandatory_fields_for_user(f_name=f_name,
                                       l_name=l_name,
                                       email=inv_email,
                                       phone=phone,
                                       pswd=pswd,
                                       pswd_conf=pswd_conf). \
        agree_pp(). \
        finish_registration(). \
        email_incorrect()


@allure.description("REQUIREMENTS - Telephone must be between 3 and 32 characters")
@allure.title("Check that impossible to register user with incorrect Telephone {inv_tlphn} and error is displayed")
@pytest.mark.parametrize('inv_tlphn', ['', '1', ' ', '1', '12', '121212121212121212121212121212121'])
def test_register_with_incorrect_telephone(browser, url, inv_tlphn):
    """Check that impossible to register user with incorrect Telephone and error is displayed"""
    l_name = 'test'
    f_name = "test"
    email = "test4@tt.qqq"
    pswd = "qwerty"
    pswd_conf = "qwerty"
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser). \
        open_account_menu(). \
        open_register_form()
    RegisterUserPage(browser). \
        fill_mandatory_fields_for_user(f_name=f_name,
                                       l_name=l_name,
                                       email=email,
                                       phone=inv_tlphn,
                                       pswd=pswd,
                                       pswd_conf=pswd_conf). \
        agree_pp(). \
        finish_registration(). \
        telephone_incorrect()


@allure.description("REQUIREMENTS - Password must be between 4 and 20 characters")
@allure.title("Check that impossible to register user with incorrect Password {inv_pswd} and error is displayed")
@pytest.mark.parametrize('inv_pswd', ['', '1', '12', '123', '121212121212121212121'])
def test_register_with_incorrect_password(browser, url, inv_pswd):
    """Check that impossible to register user with incorrect Password and error is displayed"""
    l_name = 'test'
    f_name = "test"
    email = "test4@tt.qrr"
    phone = "1231231"
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser). \
        open_account_menu(). \
        open_register_form()
    RegisterUserPage(browser). \
        fill_mandatory_fields_for_user(f_name=f_name,
                                       l_name=l_name,
                                       email=email,
                                       phone=phone,
                                       pswd=inv_pswd,
                                       pswd_conf=inv_pswd). \
        agree_pp(). \
        finish_registration(). \
        password_incorrect()


@allure.title("Check that impossible to register user with incorrect Password Confirm and error is displayed")
@pytest.mark.parametrize('inv_pswd_conf', ['', '1', '12', '123', '121212121212121212121'])
def test_register_with_incorrect_password_confirm(browser, url, inv_pswd_conf):
    """Check that impossible to register user with incorrect Password Confirm and error is displayed"""
    l_name = 'test'
    f_name = "test"
    email = "test4@tt.qri"
    pswd = "qwerty"
    phone = "1231231"
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser). \
        open_account_menu(). \
        open_register_form()
    RegisterUserPage(browser). \
        fill_mandatory_fields_for_user(f_name=f_name,
                                       l_name=l_name,
                                       email=email,
                                       phone=phone,
                                       pswd=pswd,
                                       pswd_conf=inv_pswd_conf). \
        agree_pp(). \
        finish_registration(). \
        password_confirm_incorrect()


@allure.title("Check that impossible to register user with disagreed Privacy Policy and error is displayed")
def test_register_with_unchecked_pp(browser, url):
    """Check that impossible to register user with disagreed Privacy Policy and error is displayed"""
    l_name = 'test'
    f_name = "test"
    email = "test4@tt.qrw"
    pswd = "qwerty"
    phone = "1231231"
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser). \
        open_account_menu(). \
        open_register_form()
    RegisterUserPage(browser). \
        fill_mandatory_fields_for_user(f_name=f_name,
                                       l_name=l_name,
                                       email=email,
                                       phone=phone,
                                       pswd=pswd,
                                       pswd_conf=pswd). \
        finish_registration(). \
        pp_unchecked()


@allure.title("Check user authorization with correct email {em} and incorrect password {inv_pswd} "
              "where correct password 'qwerty'")
@pytest.mark.parametrize('inv_pswd', ['QWERTY', '', '    ', 'Qwеrty'])
def test_authorization_with_incorrect_password(browser, url, inv_pswd):
    """Check user authorization with incorrect password"""
    em = 'test4@tt.ru'
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser).open_account_menu().open_login_page()
    UserLoginPage(browser).authorize_by_user(email=em, password=inv_pswd).if_authorization_incorrect()


@allure.title("Check deletion of all customers from table")
def test_delete_all_customers(browser, url):
    browser.get(f'{url}/admin')
    wait = WebDriverWait(browser, 5)
    AdminPage(browser). \
        login(username='user', password='bitnami')

    AdminHomePage(browser). \
        open_customers_menu(). \
        open_customers_list(). \
        select_all_customers(). \
        confirmed_deletion(). \
        is_table_empty()
    time.sleep(3)


@allure.title("Check error message when too much (min 6) attempts to authorize with incorrect credentials")
def test_many_attempts_to_authorize_with_incorrect_credentials(browser, url):
    """Check error message when too much (min 6) attempts to authorize with incorrect credentials"""
    em = 'test4@tt.ru'
    inv_pswd = '123123'
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    MainPage(browser).open_account_menu().open_login_page()
    i = 0
    while i < 6:
        UserLoginPage(browser).authorize_by_user(email=em, password=inv_pswd)
        i = i + 1
    UserLoginPage(browser).if_too_much_attempts()
