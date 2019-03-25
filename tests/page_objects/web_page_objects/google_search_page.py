
from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import BasePage


class GoogleSearchPage(BasePage):
    """ page object for initial Google Search page """

    def __init__(self, driver):
        super(GoogleSearchPage, self).__init__(driver)
        self._google_search_page_locators = []
        # locator(s) on initial page
        self. _search_text_field_locator = {"by": MobileBy.NAME, "value": "q"}
        self._google_search_page_locators.append(self._search_text_field_locator)
        self._google_logo_locator = {"by": MobileBy.ID, "value": "hplogoo"}
        self._google_search_page_locators.append(self._google_logo_locator)
        self._google_apps_widget_locator = {"by": MobileBy.XPATH, "value": "//div[@id='gbwa']//a[@role='button']"}
        self._google_search_page_locators.append(self._google_apps_widget_locator)
        self._search_button_locator = {"by": MobileBy.XPATH, "value": '//button[@jsaction="click:.CLIENT"]'}
        self._google_search_page_locators.append(self._search_button_locator)
        #  other locators -- not present on initial page
        self._search_result_section_locator = {"by": MobileBy.XPATH, "value": '//div[contains(@class,"srg")]//div[@data-hveid]'}
        self._search_result_link_locator = {"by": MobileBy.XPATH, "value": '//div[contains(@class,"srg")]//div[@data-hveid]//a/div[2]'}

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

    def perform_search_for_text(self, text_to_search_for):
        self._find(self._search_text_field_locator).send_keys(text_to_search_for)
        self._find(self._search_button_locator).click()

    def get_first_result_http_link(self):
        return self._find(self._search_result_link_locator).text


        


    