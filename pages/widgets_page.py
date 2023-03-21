import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.widgets_licators import AccordianLocators, AutoCompletLocatars
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianLocators

    def check_accordian(self, accordian_num):
        accordian = {'first':
                         {'title': self.locators.SECTION_FIRST,
                          'content': self.locators.SECTION_FIRST_TEXT},
                     'second':
                         {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_SECOND_TEXT},
                     'third':
                         {'title': self.locators.SECTION_THIRD,
                          'content': self.locators.SECTION_THIRD_TEXT},
                     }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]

class AutoCompletPage(BasePage):
    locators = AutoCompletLocatars

    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_visible(self.locators.MULTI_COLOR_INPUT_FIELD)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
            time.sleep(1)
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_visible(self.locators.MULTI_COLOR_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_COLOR_DELETE_BUTTON)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_visible(self.locators.MULTI_COLOR_VALUE))
        return count_value_before, count_value_after
    def remove_all_values_from_multi(self):
        count_value_before = len(self.elements_are_visible(self.locators.MULTI_COLOR_VALUE))
        delete_button = self.element_is_present(self.locators.MULTI_COLOR_DELETE_ALL_BUTTON)
        delete_button.click()
        try:
            count_value_after = len(self.elements_are_visible(self.locators.MULTI_COLOR_VALUE))
        except TimeoutException:
            count_value_after = 0
        return count_value_before, count_value_after
    def check_color_in_multi(self):
        color_list = self.elements_are_visible(self.locators.MULTI_COLOR_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def check_input_color_in_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_color = self.element_is_visible(self.locators.SINGLE_COLOR_INPUT_FIELD)
        input_color.send_keys(color)
        input_color.send_keys(Keys.ENTER)
        output_color = self.element_is_visible(self.locators.SINGLE_COLOR_VALUE).text
        return color, output_color




