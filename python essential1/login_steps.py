from behave import *


@when(u'I navigate to https://www.demo.guru99.com/V4/')
def step_impl(context):
    context.login_page.navigate_to_login()


@when(u'I enter valid userId')
def step_impl(context):
    context.login_page.enter_userid()


@when(u'I enter valid password')
def step_impl(context):
    context.login_page.enter_password()


@when(u'I click on Accept All button')
def step_impl(context):
    context.login_page.click_content()


@when(u'I click Login button')
def step_impl(context):
    context.login_page.login_button()


@then(u'The Login is successfuly done')
def step_impl(context):
    context.login_page.valid_login()
