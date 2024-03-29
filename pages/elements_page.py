import base64
import os
import random
import time
import pathlib

import allure
import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablesPageLocators, ButtonPageLocators, LinksPageLocators, DownloadPageLocators, DynamicPropertiesPageLocators
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()
    @allure.step("заполнить все поля")
    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    @allure.step("собрать данные с заполненых полей")
    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address

class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    @allure.step("открыть полный список")
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step("отметить случайные чекбоксы")
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    @allure.step("получить отмеченные чекбоксы")
    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_elements(By.XPATH, "//ancestor::span[@class='rct-title']")
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    @allure.step("подучить текст результата отмеченных чекбоксов")
    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step("выбрать одну из трех радиокнопок")
    def click_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIO,
                'impressive': self.locators.IMPRESSIVE_RADIO,
                'no': self.locators.NO_RADIO}
        self.element_is_visible(choices[choice]).click()

    @allure.step("получить текст с выбранной кнопки")
    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text

class WebTablesPage(BasePage):
    locators = WebTablesPageLocators()

    @allure.step("добавить новую персону")
    def add_new_person(self):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_RECORD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            count -= 1
            return [first_name, last_name, str(age), email,  str(salary), department]

    @allure.step("проверка созданной персоны")
    def check_new_added_person(self):
        person_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in person_list:
            data.append(item.text.splitlines())
        return data

    @allure.step("поиск персоны")
    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_IMPUT).send_keys(key_word)

    @allure.step("проверка найденой персоны")
    def check_searched_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element('xpath', ".//ancestor::div[@class='rt-tr-group']")
        return row.text.splitlines()

    @allure.step("обновление информации о лице")
    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_PERSON_INFO_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return str(age)

    @allure.step("удаление персоны")
    def delete_person_info(self):
        self.element_is_present(self.locators.DELETE_BUTTON).click()

    @allure.step("проверка удаления персоны")
    def check_delete(self):
        no_data_info = self.element_is_present(self.locators.NO_DATA_INFO)
        return no_data_info.text

    @allure.step("выбор количества строк на странице")
    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.ROW_PER_PAGE)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible(By.CSS_SELECTOR, 'option[value="{x}"]').click()
            data.append(self.check_count_rows())
        return data

    @allure.step("проверка количества строк")
    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)
class ButtonPage(BasePage):
    locators = ButtonPageLocators()

    @allure.step("выбор типа клика")
    def click_on_different_buttons(self, type_click):
        if type_click == "double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
            return self.chek_clicked_on_button(self.locators.CHECK_DOUBLE_CLICK_BUTTON)

        if type_click == "right":
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.chek_clicked_on_button(self.locators.CHECK_RIGHT_CLICK_BUTTON)

        if type_click == "click":
            self.element_is_visible(self.locators.PRIMARY_CLICK_BUTTON).click()
            return self.chek_clicked_on_button(self.locators.CHECK_PRIMARY_CLICK_BUTTON)

    @allure.step("проверка нажатой кнопки")
    def chek_clicked_on_button(self, element):
        return self.element_is_present(element).text

class LinksPage(BasePage):
    locators = LinksPageLocators()

    @allure.step("проверка открытия новой вкладки")
    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    @allure.step("проверка сломанной ссылки")
    def check_broken_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_visible(self.locators.BAD_REQUEST_LINK).clik()
        else:
            return request.status_code

    @allure.step("проверка динамической ссылки")
    def check_new_tab_dynamic_link(self):
        dynamic_link = self.element_is_visible(self.locators.DYNAMIC_LINK)
        link_href = dynamic_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            dynamic_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code
class DownloadPage(BasePage):
    locators = DownloadPageLocators()

    @allure.step("выгрузка файла")
    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_BUTTON).send_keys(path)
        os.remove(path)
        checked_path = self.element_is_present(self.locators.CHECK_UPLOAD_FILE).text
        upload_file_name = pathlib.Path(file_name).stem
        checked_path_file_name = pathlib.Path(checked_path).stem
        return upload_file_name, checked_path_file_name

    @allure.step("загрузка файла")
    def download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_BUTTON).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = rf'C:\Users\ПК\PycharmProjects\AvtoTestFrontend\testfile{random.randint(0, 999)}.jpg'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        return check_file
class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    @allure.step("временно недоступная кнопка")
    def enable_at_time_button(self):
        enable_after_button = self.element_is_visible(self.locators.ENABLE_AFTER_BUTTON)
        before_time = enable_after_button.get_attribute('disabled')
        time.sleep(6)
        after_time = enable_after_button.get_attribute('disabled')
        return before_time, after_time

    @allure.step("кнопка меняющая цвет")
    def button_change_color(self):
        color_button = self.element_is_visible(self.locators.COLOR_CHANGE_BUTTON).value_of_css_property('color')
        time.sleep(6)
        color_button_changed = self.element_is_visible(self.locators.COLOR_CHANGE_BUTTON).value_of_css_property('color')
        return color_button, color_button_changed

    @allure.step("кнопка доступная через 5 секунд")
    def check_apper_at_time(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_BUTTON)
        except TimeoutException:
            return False
        return True

