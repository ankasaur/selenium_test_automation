from selenium.webdriver.common.by import By
from .pages.login_page import LoginPage

def test_guest_should_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()