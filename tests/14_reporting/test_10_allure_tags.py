import allure


def test_without_any_annotations_that_wont_be_executed():
    pass


@allure.story('epic_1')
def test_with_epic_1():
    pass


@allure.story('story_1')
def test_with_story_1():
    pass


@allure.story('story_2')
def test_with_story_2():
    pass


@allure.feature('feature_2')
@allure.story('story_2')
def test_with_story_2_and_feature_2():
    pass


"""
following commandline options to specify different sets of tests to execute passing a list of comma-separated values:

--allure-epics
--allure-features
--allure-stories

for example:
$ pytest --alluredir=allure --clean-alluredir --allure-stories story_1,story_2
"""
