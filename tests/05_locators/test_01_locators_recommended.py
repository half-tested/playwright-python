import re


def test_recommended_locators(page):
    page.goto("http://127.0.0.1:8000/login")

    page.get_by_label("username").fill("default")                              # find by substring
    # page.get_by_label("Username:", exact=True).fill("default")               # find by exact string
    # page.get_by_label(re.compile("user\w+", re.IGNORECASE)).fill("default")  # find by regex pattern

    page.get_by_label("Password:").fill("QADqwerty")

    page.get_by_title("login").click()                                # identify element by partial title value
    # page.get_by_title("Login", exact=True).click()                  # identify element by exact title value
    # page.get_by_title(re.compile("log\wn", re.IGNORECASE)).click()  # identify element by regex pattern

    page.get_by_role("link", name="Demo Pages").click()                                 # same as below
    # page.get_by_role("link", name="demo page").click()                                # by default "name" works on contains and case non-sensitive
    # page.get_by_role("link", name="Demo pages", exact=True).click()                   # to have "name" match exactly and case-sensitive
    # page.get_by_role("link", name=re.compile("demo page\w+", re.IGNORECASE)).click()  # regex pattern works for "name"

    page.get_by_role("link", name="Demo controls").click()

    page.get_by_placeholder("entered value appears next").type("by Placeholder value entered")                # search for element with placeholder by partial value
    # page.get_by_placeholder("entered value appears next", exact=True).type("by Placeholder value entered")  # search for element with placeholder by exact value
    # page.get_by_placeholder(re.compile("entered[\s\w]+appears next")).type("by Placeholder value entered")  # serach for element with placeholder by regex pattern

    page.get_by_text("placeholder value").wait_for(timeout=3000)                               # looks for substring, i.e. partial match and case non-sensitive
    # page.get_by_text("by Placeholder value entered", exact=True).wait_for(timeout=3000)      # exact looks for exact string
    # page.get_by_text(re.compile("by [Placeholder ,value]+ entered")).wait_for(timeout=3000)  # looks for regex pattern to match

    page.get_by_alt_text("one").click()                         # alt text by partial match and case non-sensitive
    # page.get_by_alt_text("logo one", exact=True).click()      # alt text exact match
    # page.get_by_alt_text(re.compile("[lo,go]+ one")).click()  # alt text by regex pattern

    page.get_by_text("by Placeholder value entered").wait_for(state="hidden", timeout=3000)