from browser import Browser
from pages.sort import TestSortByName

def before_all(context):
    context.browser = Browser()
    context.sort = TestSortByName()


def after_all(context):
    context.browser.close()