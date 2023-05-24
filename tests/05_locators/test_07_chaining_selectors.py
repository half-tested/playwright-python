def test_locators_chaining_selectors(page):
    page.goto("http://127.0.0.1:8000/login")
    page.get_by_label("Username:").fill("default")
    page.get_by_label("Password:").fill("QADqwerty")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Test Cases").click()
    page.pause()
    # playwright.$("xpath=//table >> css=tr >> css=.PASS")                                    # capture last element in the chain
    # playwright.$("xpath=//table >> *css=tr >> css=.PASS")                                   # capture middle element in the chain due to "*"
    # playwright.$("xpath=//table >> *css=tr:has-text('default') >> css=.PASS")               # capture middle element in the chain due to "*"
    # playwright.$("xpath=//table >> css=tr:has-text('default'):has(.FAIL) >> css=.editBtn")  # capture last element in the chain
    # playwright.$("xpath=//table >> css=tr >> text='Details'")                               # capture last element in the chain
