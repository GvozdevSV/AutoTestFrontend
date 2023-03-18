import random

from selenium.webdriver.common.by import By

class BrowserWindowsPageLocators:
    TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    MESSAGE_BUTTON = (By.CSS_SELECTOR, 'button[id="messageWindowButton"]')

    CHECK_NEW_TAB = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')
    CHECK_WINDOW_TAB = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')

class AlertsPageLocators:
    ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    TIMER_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CONFIRM_BUTTON = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    PROMT_BUTTON = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    #check
    CONFIRM_RESULT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    PROMPT_RESULT = (By.CSS_SELECTOR, 'span[id="promptResult"]')

class FramesPageLocators:
    FRAME_ONE = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    FRAME_TWO = (By.CSS_SELECTOR, 'iframe[id="frame2"]')
    FRAME_TEXT = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')