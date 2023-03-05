import time

import allure

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage

@allure.suite("Elements")
class TestElements:
    @allure.feature("TextBox")
    class TestTextBox:
        @allure.title("Check TextBox")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, "ФИО не совпадает"
            assert email == output_email, "электронная почта не совпадает"
            assert current_address == output_cur_addr, "current address не совпадает"
            assert permanent_address == output_per_addr, "permanent address не совпадает"

    class TestCheckBox:
        @allure.title('Check CheckBox')
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, 'checkboxes have not been selected'
    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver,'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'not select yes'"
            assert output_impressive == 'Impressive', "'not select impressive'"
            assert output_no == 'no', "'not select no'"