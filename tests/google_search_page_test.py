
import unittest
from appium import webdriver
from page_objects.web_page_objects.google_search_page import GoogleSearchPage
from page_objects.util import Util


class GoogleSearchPageTests(unittest.TestCase):
    def setUp(self):
        desired_capabilities = Util.read_desired_capabilities_data('desired_capabilities_google.json')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

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
        
    def test_perform_sample_search_and_verify_link_in_result(self):
        google_search_page = GoogleSearchPage(self.driver)
        google_search_page.navigate_to_page()
        google_search_page.wait_for_page_to_load()
        google_search_page.perform_search_for_text("mobile integration workgroup")
        self.assertTrue("https://miwtech.com" in google_search_page.get_first_result_http_link(), "did not find {} in {}".format("https://miwtech.com", google_search_page.get_first_result_http_link()))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(GoogleSearchPageTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

