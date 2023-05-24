import allure


def test_with_no_severity_label():
    pass


@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    pass


@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity(object):

    def test_inside_the_normal_severity_test_class(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_severity_test_class_with_overriding_critical_severity(self):
        pass


"""
Severity decorator can be applied to functions, methods or entire classes.

By using --allure-severities commandline option with a list of comma-separated 
severity levels only tests with corresponding severities will be run.

$ pytest --alluredir=allure --clean-alluredir --allure-severities=critical
"""
