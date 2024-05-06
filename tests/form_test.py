import time

import allure

from pages.form_page import FormPage

@allure.suite('Form')
class TestForm:
    @allure.feature('Test form')
    class TestFormPage:
        @allure.title('Checking the field form')
        def test_form(self, driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            person_input = form_page.fill_form_fields()
            time.sleep(1)
            person_output = form_page.check_form()

            assert [person_input.first_name + " " + person_input.last_name, person_input.email] == [person_output[0], person_output[1]]
