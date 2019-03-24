
from abc import ABC, abstractmethod
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage(ABC):
    """ page object base page with common methods """

    def __init__(self, driver):
        self.driver = driver

    def _visit(self, url):
        self.driver.get(url)
    
    ## Locators supported:
    #   ID 
    #   XPATH
    #   LINK_TEXT
    #   PARTIAL_LINK_TEXT
    #   NAME
    #   TAG_NAME
    #   CLASS_NAME
    #   CSS_SELECTOR
    ## Locator syntax
    #   _locator_name = {"by": By.ID, "value": "locator_value_eg_buttonId"}

    def _find(self, locator):
        return self.driver.find_element(locator["by"], locator["value"])

    def _click(self, locator):
        self._find(locator).click()

    def _type(self, locator, input_text):
        self._find(locator).send_keys(input_text)

    def _is_displayed(self, locator):
        _display_status = False
        try:
            _display_status = self._find(locator).is_displayed()
        except NoSuchElementException:
            return False
        return _display_status

    def _wait_for_is_displayed(self, locator, timeout=5):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(
                expected_conditions.visibility_of_element_located(
                    (locator['by'], locator['value'])))
        except TimeoutException:
            return False
        return True
    
    def _wait_for_is_not_displayed(self, locator, timeout=5):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(
                expected_conditions.invisibility_of_element_located(
                    (locator['by'], locator['value'])))
        except TimeoutException:
            return False
        return True

    def _wait_for_element(self, locator, max_wait_time=5):
        WebDriverWait(self.driver, max_wait_time).until( EC.presence_of_element_located(locator)) 

    def _get_current_page_title(self):
        return self.driver.title

    def _get_current_page_url(self):
        return self.driver.current_url

    def _verify_locators(self, locators):
        for locator in locators:
            assert (self._is_displayed(locator)), "locator {} not found".format(locator)

    @abstractmethod
    def navigate_to_page(self):
        """if possible, a direct way to get to page"""
        pass

    @abstractmethod
    def wait_for_page_to_load(self, timeout=5):
        """ wait for chosen page element(s) before acting on page"""
        pass 

    @abstractmethod
    def did_successfully_load_page(self):
        """ should return true, will raise error if any item not present on page """
        pass


        