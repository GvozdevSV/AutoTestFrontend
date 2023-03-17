import random

from selenium.webdriver.common.by import By

class BrowserWindowsPageLocators:
    TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    MESSAGE_BUTTON = (By.CSS_SELECTOR, 'button[id="messageWindowButton"]')

    CHECK_NEW_TAB = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')
    CHECK_WINDOW_TAB = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')