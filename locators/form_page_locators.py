import random

from selenium.webdriver.common.by import By

class FormPageLocators:
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    GENDER_RADIOBUTTON = (By.CSS_SELECTOR, f'input[id="gender-radio-{random.randint(1, 3)}"]')
    MOBILE_NUMBER_INPUT = (By.CSS_SELECTOR, 'input[id="userNumber"]')
    DATA_INPUT = (By.CSS_SELECTOR, 'input[id="dateOfBirthInput"]')
    SUBJECTS_INPUT = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    HOBBIES = (By.CSS_SELECTOR, f'input[id="hobbies-checkbox-{random.randint(1, 3)}"]')
    UPLOAD_PICTURE = (By.CSS_SELECTOR, 'id="uploadPicture"')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    SELECT_STATE = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    SELECT_CITY = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')