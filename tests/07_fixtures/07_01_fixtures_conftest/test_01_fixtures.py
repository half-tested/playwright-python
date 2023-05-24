from pages.TestCasesPage import TestCasesPage


def test_case_change_status_check(home_page):
    existing_test = "Status change test"

    home_page.navigate_to_test_cases()

    testcases_page = TestCasesPage(home_page.page)
    test_case = testcases_page.test_case_row_by_name(existing_test)

    test_case.click_fail_button()
    assert test_case.get_status() == "FAIL", f"status should be FAIL for test '{existing_test}"''

    test_case.click_pass_button()
    assert test_case.get_status() == "PASS", f"status should be PASS for test '{existing_test}"''


def test_create_new_testcase(random_test_name, home_page):
    test_name = random_test_name
    test_description = f"description from {test_name}"
    print(f"test_name: {test_name}")
    print(f"test_description: {test_description}")

    test_case_row = home_page \
        .navigate_to_create_new_test() \
        .create_test_case(test_name, test_description) \
        .navigate_to_test_cases() \
        .test_case_row_by_name(test_name)

    assert test_case_row.is_displayed(), f"'{test_name}' is not in the test cases list"
    assert test_case_row.get_status() == "Norun", f"default status 'Norun' is not set for '{test_name}'"


def test_existing_testcase_displayed(created_test, home_page):
    print(f"test_name: {created_test}")

    test_case_row = home_page \
        .navigate_to_test_cases() \
        .test_case_row_by_name(created_test)

    assert test_case_row.is_displayed(), f"'{created_test}' is not in the test cases list"