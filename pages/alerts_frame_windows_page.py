import time

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators
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