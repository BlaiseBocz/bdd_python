from pytest_bdd import *


@given("the basket has 2 cucumbers")
def step_impl():
    raise NotImplementedError(u'STEP: Given the basket has 2 cucumbers')


@when("4 cucumbers are added to the basket")
def step_impl():
    raise NotImplementedError(u'When 4 cucumbers are added to the basket')


@then("the basket contains 6 cucumbers")
def step_impl():
    raise NotImplementedError(u' Then the basket contains 6 cucumbers')
