import random

from selenium.webdriver.common.by import By
class AccordianLocators:
    SECTION_FIRST = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    SECTION_FIRST_TEXT = (By.CSS_SELECTOR, 'div[id="section1Content"]')
    SECTION_SECOND = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECTION_SECOND_TEXT = (By.CSS_SELECTOR, 'div[id="section2Content"]')
    SECTION_THIRD = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    SECTION_THIRD_TEXT = (By.CSS_SELECTOR, 'div[id="section3Content"]')

class AutoCompletLocatars:
    MULTI_COLOR_INPUT_FIELD = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_COLOR_VALUE = (By.CSS_SELECTOR, 'div[class="css-12jo7m5 auto-complete__multi-value__label"]')
    MULTI_COLOR_DELETE_BUTTON = (By.CSS_SELECTOR, 'div[class="css-xb97g8 auto-complete__multi-value__remove"]')
    MULTI_COLOR_DELETE_ALL_BUTTON = (By.CSS_SELECTOR, 'div[class="auto-complete__indicators css-1wy0on6"]')

    SINGLE_COLOR_INPUT_FIELD = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
    SINGLE_COLOR_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')
class DatePageLocators:
    DATE_FIELD = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    DATE_MONTH_SELECT = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    DATE_YEAR_SELECT = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DATE_DAY_SELECT = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

    DATE_AND_TIME_FIELD = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATE_AND_TIME_MONTH_SELECT = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]]')
    DATE_AND_TIME_YEAR_SELECT = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')
    DATE_AND_TIME_DAY_SELECT = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')
    TIME_SELECT = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')