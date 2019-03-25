
from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import BasePage
from appium.webdriver.common.touch_action import TouchAction


class ComposeMailPage(BasePage):
    """ page object for compose mail page """

    def __init__(self, driver):
        super(ComposeMailPage, self).__init__(driver)
        self._compose_mail_page_locators = []
        # locator(s) on initial page  -- {"by": MobileBy.ID, "value": ""}
        self._back_button_locator = {"by": MobileBy.ACCESSIBILITY_ID, "value": "Back"}
        self._compose_mail_page_locators.append(self._back_button_locator)

        self._send_button_locator = {"by": MobileBy.ID, "value": "com.aol.mobile.aolapp:id/menu_send_message"}
        self._compose_mail_page_locators.append(self._send_button_locator)

        self._to_address_text_field_locator = {"by": MobileBy.ID, "value": "com.aol.mobile.aolapp:id/email_field"}
        self._compose_mail_page_locators.append(self._to_address_text_field_locator)

        self._subject_text_field_locator = {"by": MobileBy.ID, "value": "com.aol.mobile.aolapp:id/subject_view"}
        self._compose_mail_page_locators.append(self._subject_text_field_locator)

        self._message_body_text_field_locator = {"by": MobileBy.ID, "value": "com.aol.mobile.aolapp:id/message_body_view"}
        self._compose_mail_page_locators.append(self._message_body_text_field_locator)

    def navigate_to_page(self):
        # doesn't apply on this page
        pass

    def wait_for_page_to_load(self, timeout=10):
        return self._wait_for_is_displayed(self._send_button_locator, timeout)

    def did_successfully_load_page(self):
        self._verify_locators(self._compose_mail_page_locators)
        return True 

    def fill_in_new_mail_message_and_send(self, email_address, subject_text, body_text):
        self._find(self._to_address_text_field_locator).send_keys(email_address)
        self._find(self._subject_text_field_locator).send_keys(subject_text)
        self._find(self._message_body_text_field_locator).send_keys(body_text)
        self._find(self._send_button_locator).click()


        


    