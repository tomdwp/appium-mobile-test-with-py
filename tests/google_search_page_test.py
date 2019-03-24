

import unittest, time
from appium import webdriver
from page_objects.web_page_objects.google_search_page import GoogleSearchPage


class GoogleSearchPageTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'ANDROID',
            'automationName': 'UiAutomator2',
            'deviceName': 'Pixel 2 API Q',
            'browserName': 'Chrome'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_loading_secure_page(self):
        google_search_page = GoogleSearchPage(self.driver)
        google_search_page.navigate_to_page()
        google_search_page.wait_for_page_to_load()
        self.assertTrue(google_search_page.did_successfully_load_page())
        
    def test_loading_insecure_page(self):
        google_search_page = GoogleSearchPage(self.driver)
        google_search_page.navigate_to_insecure_page()
        google_search_page.wait_for_page_to_load()
        self.assertTrue(google_search_page.did_successfully_load_page()) 
        #google_search_page._tap_to_place_cursor_in_search_field()       
        time.sleep(5)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(GoogleSearchPageTests)
    unittest.TextTestRunner(verbosity=2).run(suite)