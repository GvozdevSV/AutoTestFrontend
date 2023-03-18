import random
import time

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])#запомнить переход на новую вкладку
        new_tab_text = self.element_is_present(self.locators.CHECK_NEW_TAB).text
        return new_tab_text

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])#запомнить переход на новую вкладку
        new_window_text = self.element_is_present(self.locators.CHECK_WINDOW_TAB).text
        return new_window_text

class AlertPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_alert_after_5_second(self):
        self.element_is_visible(self.locators.TIMER_ALERT_BUTTON).click()
        time.sleep(5)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()           #запомнить
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT)
        return text_result.text

    def check_prompt_alert(self):
        text = f'avtotest{random.randint(0,99)}'
        self.element_is_visible(self.locators.PROMT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()           #запомнить
        text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
        return text_result, text

class FramePage(BasePage):
    locators = FramesPageLocators()

    def check_frame(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FRAME_ONE)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.FRAME_TEXT).text
            self.driver.switch_to.default_content()
            return text, width, height
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.FRAME_TWO)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.FRAME_TEXT).text
            self.driver.switch_to.default_content()
            return text, width, height




