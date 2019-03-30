

import unittest, time
from appium import webdriver
from page_objects.aol_mail_page_objects.home_tab_page import HomeTabPage
from page_objects.aol_mail_page_objects.mail_tab_page import MailTabPage
from page_objects.util import Util

class AolMailAppTests(unittest.TestCase):
    def setUp(self):
        desired_capabilities = Util.read_desired_capabilities_data('desired_capabilities_aol.json')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

    def tearDown(self):
        self.driver.close_app()
        self.driver.remove_app('com.aol.mobile.aolapp')
        self.driver.quit()

    def test_app_on_initial_launch(self):
        home_tab_page = HomeTabPage(self.driver)
        home_tab_page.wait_for_page_to_load()
        self.assertTrue(home_tab_page.did_successfully_load_page())
        home_tab_page.tab_bar.navigate_to_mail_tab()
        mail_tab_page = MailTabPage(self.driver)
        mail_tab_page.wait_for_signin_modal_page_to_load()
        mail_tab_page.signin_to_mail('miw_mobile@aol.com', 'M0bil3@123')
        mail_tab_page.wait_for_page_to_load()
        self.assertTrue(mail_tab_page.did_successfully_load_page())

        
    

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AolMailAppTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

