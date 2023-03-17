import os
import time

from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(person.first_name)
        self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER_RADIOBUTTON).click()
        self.element_is_visible(self.locators.MOBILE_NUMBER_INPUT).send_keys(person.mobile_namber)
        self.element_is_visible(self.locators.SUBJECTS_INPUT).send_keys('Maths')
        self.element_is_visible(self.locators.SUBJECTS_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_visible(self.locators.UPLOAD_PICTURE).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.SELECT_STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.SELECT_CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return person

    def check_form(self):
        form_result = self.elements_are_present(self.locators.CHECK_TABLE)
        data = []
        for item in form_result:
            self.go_to_element(item)
            data.append(item.text)
        return data













