from browser import Browser
from pages.login_page import TestLogin


def before_all(context):
    context.browser = Browser()
    context.login_page = TestLogin()


def after_all(context):
    context.browser.close()
