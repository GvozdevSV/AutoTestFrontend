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

class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")

class RadioButtonPageLocators:
    YES_RADIO = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="yesRadio"]')
    IMPRESSIVE_RADIO = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="impressiveRadio"]')
    NO_RADIO = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'p span[class="text-success"]')

class WebTablesPageLocators:
    #add person
    ADD_RECORD_BUTTON = (By.CSS_SELECTOR, '#addNewRecordButton')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#lastName')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#userEmail')
    AGE_INPUT = (By.CSS_SELECTOR, '#age')
    SALARY_INPUT = (By.CSS_SELECTOR, '#salary')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, '#department')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#submit')
    #get table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')
    #search
    SEARCH_IMPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')

    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    UPDATE_PERSON_INFO_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')
    NO_DATA_INFO = (By.CSS_SELECTOR, 'div[class="rt-noData"]')
    ROW_PER_PAGE = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')

class ByuttonPageLocators:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    PRIMARY_CLICK_BUTTON = (By.XPATH, '//div[3]/button')
    #check
    CHECK_DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    CHECK_RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    CHECK_PRIMARY_CLICK_BUTTON = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')