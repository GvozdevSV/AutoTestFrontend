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
class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    PARENT_FRAME_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_FRAME_TEXT = (By.CSS_SELECTOR, 'p')

class ModalDialogLocators:
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showSmallModal"]')
    SMALL_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[id="closeSmallModal"]')
    TITLE_SMALL_MODAL_WINDOW = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-sm"]')
    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showLargeModal"]')
    LARGE_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[id="closeLargeModal"]')
    TITLE_LARGE_MODAL_WINDOW = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-lg"]')

    TEXT_MODAL_WINDOW = (By.CSS_SELECTOR, 'div[class="modal-body"]')
    X_CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[class="close"]')
