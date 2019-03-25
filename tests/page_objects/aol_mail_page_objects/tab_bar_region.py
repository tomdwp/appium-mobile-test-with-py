from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import BasePage



class TabBarRegion(BasePage):
    """ page object for tab bar region of page """

    def __init__(self, driver):
        super(TabBarRegion, self).__init__(driver)
        self._tab_bar_region_locators = []
        # locator(s) on initial page  -- {"by": MobileBy.ID, "value": ""}
        self._mail_tab_locator = {"by": MobileBy.ID, "value": "com.aol.mobile.aolapp:id/menubar_mail"}
        self._tab_bar_region_locators.append(self._mail_tab_locator)

        self._home_tab_locator = {"by": MobileBy.ID, "value": "com.aol.mobile.aolapp:id/menubar_home"}
        self._tab_bar_region_locators.append(self._home_tab_locator)
        
        self._video_tab_locator = {"by": MobileBy.ID, "value": "com.aol.mobile.aolapp:id/menubar_video"}
        self._tab_bar_region_locators.append(self._video_tab_locator)
        
        self._search_tab_locator = {"by": MobileBy.ID, "value": "com.aol.mobile.aolapp:id/menubar_search"}
        self._tab_bar_region_locators.append(self._search_tab_locator)
        
        self._settings_tab_locator = {"by": MobileBy.ID, "value": "com.aol.mobile.aolapp:id/menubar_settings"}
        self._tab_bar_region_locators.append(self._settings_tab_locator)

    @property
    def mail(self):
        return self._find(self._mail_tab_locator)

    @property
    def mail_locator(self):
        ## this is a small hack to allow the 'home tab page' to have a locator to wait for
        return self._mail_tab_locator

    @property
    def home(self):
        return self._find(self._home_tab_locator)

    @property
    def video(self):
        return self._find(self._video_tab_locator)

    @property
    def search(self):
        return self._find(self._search_tab_locator)

    @property
    def settings(self):
        return self._find(self._settings_tab_locator)

    def get_locators(self):
        return self._tab_bar_region_locators

    def navigate_to_page(self):
        pass

    def wait_for_page_to_load(self):
        pass
        
    def did_successfully_load_page(self):
        pass

    def navigate_to_mail_tab(self):
        self._tap(self._mail_tab_locator)

    def navigate_to_home_tab(self):
        self._tap(self._home_tab_locator)

    def navigate_to_video_tab(self):
        self._tap(self._video_tab_locator)

    def navigate_to_search_tab(self):
        self._tap(self._search_tab_locator)

    def navigate_to_settings_tab(self):
        self._tap(self._settings_tab_locator)
        
    