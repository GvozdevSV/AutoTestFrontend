import random
import time

import allure

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    @allure.step("проверка открытия новой вкладки")
    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])#запомнить переход на новую вкладку
        new_tab_text = self.element_is_present(self.locators.CHECK_NEW_TAB).text
        return new_tab_text

    @allure.step("проверка открытия нового окна")
    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])#запомнить переход на новую вкладку
        new_window_text = self.element_is_present(self.locators.CHECK_WINDOW_TAB).text
        return new_window_text

class AlertPage(BasePage):
    locators = AlertsPageLocators()

    @allure.step("проверка открытия алерта")
    def check_see_alert(self):
        self.element_is_visible(self.locators.ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    @allure.step("проверка алерта через 5 секунд")
    def check_alert_after_5_second(self):
        self.element_is_visible(self.locators.TIMER_ALERT_BUTTON).click()
        time.sleep(5)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    @allure.step("проверка алерта с согласием")
    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()           #запомнить
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT)
        return text_result.text

    @allure.step("проверка алерта с вводом текста")
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

    @allure.step("проверка фреймов")
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
class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    @allure.step("проверка фрейма")
    def check_nested_frames(self, age_frame):
        if age_frame == 'parents_frame':
            frame = self.element_is_present(self.locators.PARENT_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.PARENT_FRAME_TEXT).text
            self.driver.switch_to.default_content()
            return text, width, height
        if age_frame == 'child_frame':
            parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
            self.driver.switch_to.frame(parent_frame)
            frame = self.element_is_present(self.locators.CHILD_FRAME)
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.CHILD_FRAME_TEXT).text
            self.driver.switch_to.default_content()
            return text

class ModalDialogsPage(BasePage):
    locators = ModalDialogLocators()

    @allure.step("проверка малого и большого диалога")
    def open_get_title_close(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        small_modal_title = self.element_is_visible(self.locators.TITLE_SMALL_MODAL_WINDOW).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        large_modal_title = self.element_is_visible(self.locators.TITLE_LARGE_MODAL_WINDOW).text
        self.element_is_visible(self.locators.LARGE_MODAL_CLOSE_BUTTON).click()
        print(small_modal_title)
        print(large_modal_title)
        return small_modal_title, large_modal_title





