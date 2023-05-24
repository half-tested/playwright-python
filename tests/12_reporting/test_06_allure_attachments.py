import allure


def test_multiple_attachments():
    allure.attach('simple text attachment', 'blah blah blah blah',
                  allure.attachment_type.TEXT)
    allure.attach.file('requirements.txt', attachment_type=allure.attachment_type.TEXT)
    allure.attach('<head></head><body> a page </body>', 'Attach with HTML type', allure.attachment_type.HTML)