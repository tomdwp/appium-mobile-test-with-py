
from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import BasePage
from appium.webdriver.common.touch_action import TouchAction



class GoogleSearchPage(BasePage):
    """ page object for initial Google Search page """

    def __init__(self, driver):
        super(GoogleSearchPage, self).__init__(driver)
        self._google_search_page_locators = []
        # locator(s)
        self. _search_text_field_locator = {"by": MobileBy.NAME, "value": "q"}
        self._google_search_page_locators.append(self._search_text_field_locator)
        self._google_logo_locator = {"by": MobileBy.ID, "value": "hplogoo"}
        self._google_search_page_locators.append(self._google_logo_locator)
        self._google_apps_widget_locator = {"by": MobileBy.XPATH, "value": "//div[@id='gbwa']//a[@role='button']"}
        self._google_search_page_locators.append(self._google_apps_widget_locator)
        # 
        self._page_url = 'https://www.google.com'
        self._insecure_page_url = 'http://www.google.com'

    
    def navigate_to_page(self):
        self._visit(self._page_url)

    def wait_for_page_to_load(self):
        return self._wait_for_is_displayed(self._search_text_field_locator)

    def did_successfully_load_page(self):
        self._verify_locators(self._google_search_page_locators)
        return (self._page_url in self._get_current_page_url())

    def navigate_to_insecure_page(self):
        self._visit(self._insecure_page_url)

    def _tap_to_place_cursor_in_search_field(self):
        actions = TouchAction(self.driver)
        actions.tap(self._find(self._search_text_field_locator))
        #actions.perform()


    