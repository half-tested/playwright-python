import allure


@allure.link("https://your.test_with_link.com")
def test_with_link():
    pass


@allure.link("https://your.test_with_named_link.com", name='Click me')
def test_with_named_link():
    pass


@allure.issue("DEF-140")
def test_with_issue_link():
    """
    @allure.issue will provide a link with a small bug icon. This descriptor takes test case id as the input parameter
    to use it with provided link template for issue link type. Link templates are specified in
    --allure-link-pattern configuration option for Pytest. Link templates and types have to be specified using a colon:

    $ pytest directory_with_tests/ --alluredir=/tmp/my_allure_report \
     --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
    Template keywords are issue, link and test_case to provide a template for the corresponding type of link.
    """
    pass


@allure.testcase("TC-230")
def test_with_testcase_link():
    pass

"""
pytest --alluredir=allure --clean-alluredir -k test_09_allure_links.py \
--allure-link-pattern=issue:http://www.mytesttracker.com/issue/{} \
--allure-link-pattern=tms:http://www.mytesttracker.com/tms/{}
"""