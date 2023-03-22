import time

from pages.widgets_page import AccordianPage, AutoCompletPage, DatePage


class TestAccordian:
    def test_accordion(self, driver):
        accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
        accordian_page.open()
        first_title, first_content = accordian_page.check_accordian('first')
        second_title, second_content = accordian_page.check_accordian('second')
        third_title, third_content = accordian_page.check_accordian('third')
        assert first_title == 'What is Lorem Ipsum?' and first_content > 0, 'Incorrect title or missing text'
        assert second_title == 'Where does it come from?' and second_content > 0, 'Incorrect title or missing text'
        assert third_title == 'Why do we use it?' and third_content > 0, 'Incorrect title or missing text'
class TestAutoComplete:
    def test_autocomplete(self, driver):
        auto_complete_page = AutoCompletPage(driver, 'https://demoqa.com/auto-complete')
        auto_complete_page.open()
        colors = auto_complete_page.fill_input_multi()
        colors_result = auto_complete_page.check_color_in_multi()
        assert colors == colors_result, "Not all colors add to fill"

    def test_delete_color(self, driver):
        auto_complete_page = AutoCompletPage(driver, 'https://demoqa.com/auto-complete')
        auto_complete_page.open()
        auto_complete_page.fill_input_multi()
        count_value_before, count_value_after = auto_complete_page.remove_value_from_multi()
        assert count_value_before > count_value_after, "Color are not delete"
    def test_delete_all_colors(self, driver):
        auto_complete_page = AutoCompletPage(driver, 'https://demoqa.com/auto-complete')
        auto_complete_page.open()
        auto_complete_page.fill_input_multi()
        count_value_before, count_value_after = auto_complete_page.remove_all_values_from_multi()
        assert count_value_before > 0
        assert count_value_after == 0, "Colors are not deleted"

    def test_check_single_color(self, driver):
        auto_complete_page = AutoCompletPage(driver, 'https://demoqa.com/auto-complete')
        auto_complete_page.open()
        color, output_color = auto_complete_page.check_input_color_in_single()
        assert color == [output_color], "Input and output colors not equal"

class TestDate:

    def test_chenge_date(self, driver):
        data_page = DatePage(driver, 'https://demoqa.com/date-picker')
        data_page.open()
        date_before, date_after = data_page.check_date()
        assert date_before != date_after


    #def test_chenge_date_and_time(self, driver):
        #data_page = DatePage(driver, 'https://demoqa.com/date-picker')
        #data_page.open()
        #data_page.check_date()