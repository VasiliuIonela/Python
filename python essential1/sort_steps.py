from behave import *


@when(u'I go to http://live.techpanda.org/index.php/')
def step_impl(context):
    context.sort.navigate_to_site()


@when(u'I click on \'MOBILE\' page')
def step_impl(context):
    context.sort.click_mobile()


@when(u'I select \'SORT BY\' dropdown as \'name\'')
def step_impl(context):
    context.sort.click_sort_by()


@then(u'I should see a sorted mobile list by name')
def step_impl(context):
    context.sort.sort_by_name()
