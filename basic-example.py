from selenium import selenium
import unittest
import os

class sauce(unittest.TestCase):
    def setUp(self):
        self.browser = selenium(
            'saucelabs.com',
            4444,
            """{\
                "username": "%(SAUCEUSERNAME)s",\
                "access-key": "%(SAUCEACCESSKEY)s",\
                "os": "Windows 2003",\
                "browser": "firefox",\
                "browser-version": "3.",\
                "name": "This is an example test"\
               }""" % (os.environ),
            'http://saucelabs.com')
        self.browser.start()
        self.browser.set_timeout(90000)

    def test_sauce(self):
        browser = self.browser
        browser.open("/")
        assert "Sauce Labs" in browser.get_title()

    def tearDown(self):
        self.browser.stop()

if __name__ == "__main__":
    unittest.main()
