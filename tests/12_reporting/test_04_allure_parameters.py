import allure
import pytest


@allure.step
def simple_step(step_param1, step_param2=None):
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


@pytest.mark.parametrize('param1', [True, False], ids=['id explaining value 1', 'id explaining value 2'])
def test_parameterize_with_id(param1):
    simple_step(param1)


@pytest.mark.parametrize('param1', [True, False])
@pytest.mark.parametrize('param2', ['value 1', 'value 2'])
def test_parametrize_with_two_parameters(param1, param2):
    simple_step(param1, param2)


@pytest.mark.parametrize('param1', [True], ids=['boolean parameter id'])
@pytest.mark.parametrize('param2', ['value 1', 'value 2'])
@pytest.mark.parametrize('param3', [1])
def test_parameterize_with_uneven_value_sets(param1, param2, param3):
    simple_step(param1, param3)
    simple_step(param2)


def test_parameter_recorded_from_test():
    allure.dynamic.parameter(name="param_from_test", value="created")
    step_with_nested_steps()
