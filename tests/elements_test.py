import pathlib
import random
import time

import allure

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage, ButtonPage, LinksPage, \
    DownloadPage


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

    class TestWebTables:
        def test_web_tables_add_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            new_person = web_tables_page.add_new_person()
            table_result = web_tables_page.check_new_added_person()
            assert new_person in table_result
        def test_web_tables_search_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            key_word = web_tables_page.add_new_person()[random.randint(0, 5)]
            web_tables_page.search_some_person(key_word)
            table_result = web_tables_page.check_searched_person()
            assert key_word in table_result, 'key not found'
        def test_web_tables_update_person_info(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            last_name = web_tables_page.add_new_person()[1]
            web_tables_page.search_some_person(last_name)
            age = web_tables_page.update_person_info()
            row = web_tables_page.check_searched_person()
            assert age in row

        def test_web_tables_delete_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            email = web_tables_page.add_new_person()[3]
            web_tables_page.search_some_person(email)
            web_tables_page.delete_person_info()
            text = web_tables_page.check_delete()
            assert text == "No rows found"

        def test_web_tables_change_count_row(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            count = web_tables_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], 'The number of row in table has not been changed or has chnge incorrectly'

    class TestButtonPage:

        def test_different_click_on_buttons(self, driver):
            button_page = ButtonPage(driver, 'https://demoqa.com/buttons')
            button_page .open()
            double = button_page.click_on_different_buttons('double')
            right = button_page.click_on_different_buttons('right')
            click = button_page.click_on_different_buttons('click')
            assert double == 'You have done a double click', 'The double click button not pressed'
            assert right == 'You have done a right click', 'The right click button not pressed'
            assert click == 'You have done a dynamic click', 'The click button not pressed'

    class TestLinks:

        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, "the link works or the status code in son 400"

        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400, "the link works or the status code in son 400"

        def test_dynamic_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_dynamic_link()
            assert href_link == current_url

    class TestUploadAndDownloadFile:

        def test_upload_file(self, driver):
            upload_page = DownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_page.open()
            upload_file_name, checked_path_file_name = upload_page.upload_file()
            assert upload_file_name == checked_path_file_name

        def test_download_file(self, driver):
            download_page = DownloadPage(driver, 'https://demoqa.com/upload-download')
            download_page.open()
