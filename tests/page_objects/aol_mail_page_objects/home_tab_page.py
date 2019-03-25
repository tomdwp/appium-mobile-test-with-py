
from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import BasePage
from appium.webdriver.common.touch_action import TouchAction
from .tab_bar_region import TabBarRegion


class HomeTabPage(BasePage):
    """ page object for initial AOL Mail App page """

    def __init__(self, driver):
        super(HomeTabPage, self).__init__(driver)
        self._main_app_page_locators = []
        # locator(s) on initial page  -- {"by": MobileBy.ID, "value": ""}
        
        
    
    @property
    def tab_bar(self):
        return TabBarRegion(self.driver)
        

    def navigate_to_page(self):
        pass #self._visit(self._page_url)

    def wait_for_page_to_load(self):
        return self._wait_for_is_displayed(self.tab_bar.mail_locator)

    def did_successfully_load_page(self):
        self._verify_locators(self.tab_bar.get_locators())
        return True #(self._page_url in self._get_current_page_url())

    


        


    