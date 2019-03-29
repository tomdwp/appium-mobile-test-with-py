
from appium.webdriver.common.mobileby import MobileBy
from page_objects.base_page import BasePage
from appium.webdriver.common.touch_action import TouchAction


class MailTabPage(BasePage):
    """ page object for mail tab page """

    def __init__(self, driver):
        super(MailTabPage, self).__init__(driver)
        self._mail_tab_page_locators = []
        # locator(s) on initial page  -- {"by": MobileBy.ID, "value": ""}
        self._mailbox_folders_hamburger_menu_locator = {"by": MobileBy.ACCESSIBILITY_ID, "value": "View folder list"}
        self._mail_tab_page_locators.append(self._mailbox_folders_hamburger_menu_locator)
        self._mailbox_search_button_locator = {"by": MobileBy.ID, "value": "com.aol.mobile.aolapp:id/action_search"}
        self._mail_tab_page_locators.append(self._mailbox_search_button_locator)
        self._compose_button_locator = {"by": MobileBy.ID, "value": "com.aol.mobile.aolapp:id/mail_fab"}
        self._mail_tab_page_locators.append(self._compose_button_locator)

        ## locators for signin modal
        #self._close_signin_modal_button_locator = {"by": MobileBy.ID, "value": "com.android.chrome:id/close_button"}
        self._close_signin_modal_button_locator = {"by": MobileBy.ACCESSIBILITY_ID, "value": "Navigate up"}
        self._signin_toolbar_locator = {"by": MobileBy.ID, "value": "com.aol.mobile.aolapp:id/toolbar"}

        ## locators for username signin webview 
        ### whole frame:  com.aol.mobile.aolapp:id/action_bar_root
        ### sub-frame that's about the same: android:id/content
        ### top_bar:  com.aol.mobile.aolapp:id/toolbar
        ##
        ### webview -- xpath:  /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView
        ### login webview inside webview -- xpath:  /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView

        ### view enclosing the signin text field -- id:  username-country-code-field
        self._signin_username_text_field_locator = {"by": MobileBy.ID, "value": "login-username"}
        self._signin_username_button_locator = {"by": MobileBy.ID, "value": "login-signin"}

        ## locators for password signin window
        self._signin_password_text_field_locator = {"by": MobileBy.ID, "value": "login-passwd"}
        self._signin_password_button_locator = {"by": MobileBy.ID, "value": "login-signin"}
        self._signin_forgot_password_link_locator = {"by": MobileBy.ID, "value": "mbr-forgot-link"}

        ## access_contacts_permission_modal
        self._access_contacts_permission_message_locator = {"by": MobileBy.ID, "value": "com.android.permissioncontroller:id/permission_message"}
        self._access_contacts_permission_allow_button_locator = {"by": MobileBy.ID, "value": "com.android.permissioncontroller:id/permission_allow_button"}
        self._access_contacts_permission_deny_button_locator = {"by": MobileBy.ID, "value": "com.android.permissioncontroller:id/permission_deny_button"}

        ## 2nd access_contacts_permission_modal
        self._second_access_contacts_permission_icon_locator = {"by": MobileBy.ID, "value": "android:id/icon"}
        self._second_access_contacts_permission_message_locator = {"by": MobileBy.ID, "value": "android:id/message"}
        self._second_access_contacts_permission_do_it_later_button_locator = {"by": MobileBy.ID, "value": "android:id/button2"}
        self._second_access_contacts_permission_allow_access_button_locator = {"by": MobileBy.ID, "value": "android:id/button1"}

    def navigate_to_page(self):
        # doesn't apply on this page
        pass

    def wait_for_page_to_load(self, timeout=10):
        return self._wait_for_is_displayed(self._compose_button_locator, timeout)

    def wait_for_signin_modal_page_to_load(self, timeout=10):
        return self._wait_for_is_displayed(self._close_signin_modal_button_locator, timeout)

    def did_successfully_load_page(self):
        self._verify_locators(self._mail_tab_page_locators)
        return True 

    def _switch_to_webview_frame(self):
        contexts = self.driver.contexts
        print("\ncontexts: {}".format(contexts))
        for el in self.driver.find_elements_by_xpath("//*"):
            print(el)
        self.driver.switch_to.context(contexts[-1])

    def _switch_out_of_webview_frame(self):
        contexts = self.driver.contexts
        self.driver.switch_to.context(contexts[0])

    def signin_to_mail(self, username, password):
        """sign into mail account - must already have waited for signin modal page to load"""
        if self._is_displayed(self._close_signin_modal_button_locator):
            ## signin webview currently displayed, but need to switch to it
            self._switch_to_webview_frame()
            self._wait_for_is_displayed(self._signin_username_text_field_locator)
            self._find(self._signin_username_text_field_locator).send_keys(username)
            self._find(self._signin_username_button_locator).click()
            self._wait_for_is_displayed(self._signin_password_text_field_locator)
            self._find(self._signin_password_text_field_locator).send_keys(password)
            self._find(self._signin_password_button_locator).click()
            self._switch_out_of_webview_frame()

    def compose_new_mail_message(self):
        self._find(self._compose_button_locator).click()
        if self._is_displayed(self._access_contacts_permission_message_locator):
            self._find(self._access_contacts_permission_deny_button_locator).click()
        if self._is_displayed(self._second_access_contacts_permission_message_locator):
            self._find(self._second_access_contacts_permission_do_it_later_button_locator).click()


    


        


    