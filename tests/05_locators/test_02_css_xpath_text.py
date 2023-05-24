def test_css_xpath_locators(page):
    page.goto("http://127.0.0.1:8000/login")
    page.locator("css=#id_username").fill("default")
    page.locator("xpath=//input[@name='password']").fill("QADqwerty")
    page.locator("input[type='submit']").click()      # still css without prefix "css="
    page.locator("//a[text()='Test Cases']").click()  # still xpath without prefix "xpath="


def test_more_css_locators(page):
    page.goto("http://127.0.0.1:8000/login")
    page.pause()
    page.locator("p:has-text('username') input").fill("default")             # :has-text()
    page.locator("p:has(label[for='id_password']) input").fill("QADqwerty")  # :has()
    page.locator("input:below(#id_password)").click()                        # :below()
    page.locator(".menuBox :text('Test Cases')").click()                     # :text()
    page.locator(":nth-match(table tr:has-text('default'), 2)").wait_for()   # :nth-match(selector,n)
    page.pause()


def test_text_locators(page):
    page.goto("http://127.0.0.1:8000/login")
    page.locator("text=Username").fill("default")
    page.locator("text=Password").fill("QADqwerty")
    page.pause()
    page.locator("text=/Log\s*in/i").click()   # regex may be used with text locator
    page.locator("text='Test Cases'").click()  # quoted text for full match and not quoted for partial match
