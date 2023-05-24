def test_css_xpath_locators(page) -> None:
    page.goto("http://127.0.0.1:8000/login")
    page.locator("css=#id_username").fill("alice")
    page.locator("xpath=//input[@name='password']").fill("Qamania123")
    page.locator("input[type='submit']").click()  # still css without prefix "css="
    page.locator("//a[text()='Demo controls']").click()  # still xpath without prefix "xpath="
    page.locator("div.demoSelect select").select_option("World")
    page.locator("//div[@class='logo']").click()


def test_more_css_locators(page) -> None:
    page.goto("http://127.0.0.1:8000/login")
    page.pause()
    page.locator("p:has-text('username') input").fill("alice")  # :has-text()
    page.locator("p:has(label[for='id_password']) input").fill("Qamania123")  # :has()
    page.locator("input:below(#id_password)").click()  # :below()
    page.locator(".menuBox :text('Test Cases')").click()  # :text()
    page.locator(":nth-match(table tr:has-text('alice'), 3)").wait_for(timeout=1000)  # :nth-match(selector,n)


def test_text_locators(page) -> None:
    page.goto("http://127.0.0.1:8000/login")
    page.locator("css=#id_username").fill("alice")
    page.locator("xpath=//input[@name='password']").fill("Qamania123")
    page.locator("text=/Log\s*in/i").click()  # regex may be used with text locator
    page.locator("text='Test Cases'").click()  # quoted text for full match and not quoted for partial match
    page.pause()