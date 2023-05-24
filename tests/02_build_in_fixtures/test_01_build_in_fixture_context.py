def test_context(context):  # provides instance of context to create pages
    page_one = context.new_page()
    page_one.goto("https://www.google.com/")
    page_two = context.new_page()
    page_two.goto("https://www.bing.com/")

