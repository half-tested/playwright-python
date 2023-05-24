import allure


@allure.step
def passing_step():
    pass


@allure.step
def step_with_nested_steps():
    nested_step()


@allure.step
def nested_step():
    nested_step_with_arguments(1, 'abc')


@allure.step
def nested_step_with_arguments(arg1, arg2):
    pass


def test_with_nested_steps():
    passing_step()
    step_with_nested_steps()


@allure.step('Step with placeholders in the title, positional: "{0}", keyword: "{key}"')
def step_with_title_placeholders(arg1, key=None):
    pass


def test_steps_with_placeholders():
    step_with_title_placeholders(1, key='something')
    step_with_title_placeholders(2)
    step_with_title_placeholders(3, 'anything')
