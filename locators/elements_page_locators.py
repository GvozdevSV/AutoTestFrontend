from selenium.webdriver.common.by import By

class TextBoxPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, "#userName")
    EMAIL = (By.CSS_SELECTOR, "#userEmail")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#permanentAddress")
    SUBMIT = (By.CSS_SELECTOR, "#submit")

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "p.mb-1:nth-child(3)")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "p.mb-1:nth-child(4)")

#class CheckBoxPageLocators:
   # EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button.rct-option:nth-child(1)")
    #ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
   # CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    #TITLE_ITEM = ".//ancestor::span[@class='rct-title']"
