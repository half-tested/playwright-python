def test_browser_channel(browser_channel):  # provides value of argument --browser-channel
    assert browser_channel == "chrome"      # pytest -k test_browser_channel --browser-channel chrome

