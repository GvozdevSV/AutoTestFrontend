import time

from pages.widgets_page import AccordianPage, AutoCompletPage, DatePage, SliderPage, ProgressBarPage, TabsPage, \
    ToolsTipsPage


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

    def test_change_date(self, driver):
        data_page = DatePage(driver, 'https://demoqa.com/date-picker')
        data_page.open()
        date_before, date_after = data_page.check_date()
        assert date_before != date_after, "Date not change"


    #def test_chenge_date_and_time(self, driver):
        #data_page = DatePage(driver, 'https://demoqa.com/date-picker')
        #data_page.open()
        #data_page.check_date()

class TestSlider:
    def test_check_slider(self,driver):
        slider_page = SliderPage(driver, 'https://demoqa.com/slider')
        slider_page.open()
        input_value, output_value = slider_page.check_slider()
        assert input_value != output_value, "Slider not move"

class TestProgressBar:
    def test_check_progress_bar(self, driver):
        progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
        progress_bar_page.open()
        input_value, output_value = progress_bar_page.check_progress_bar()
        assert input_value < output_value, "Not an progress"

    def test_check_return(self, driver):
        progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
        progress_bar_page.open()
        bar_value, output_bar_value = progress_bar_page.check_retry_button()
        assert bar_value > '0', "Bar not progress"
        assert output_bar_value == '0', "Bar not reset"

class TestTabsPage:
    def test_check_tabs(self, driver):
        tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
        tabs_page.open()
        what_title, what_text = tabs_page.check_tabs('what')
        origin_title, origin_text = tabs_page.check_tabs('origin')
        use_title, use_text = tabs_page.check_tabs('use')
        more_title, more_text = tabs_page.check_tabs('more')
        assert what_title == 'What' and origin_text != '0', 'the tab "what" was not pressed or the text is missing'
        assert origin_title == 'Origin' and origin_text != '0', 'the tab "Origin" was not pressed or the text is missing'
        assert use_title == 'Use' and use_text != '0', 'the tab "Use" was not pressed or the text is missing'
        assert more_title == 'More' and more_text != '0', 'the tab "More" was not pressed or the text is missing'

class TestToolsTipsPage:
    def test_check_tabs(self, driver):
        tools_tips_page = ToolsTipsPage(driver, 'https://demoqa.com/tool-tips')
        tools_tips_page.open()
        button_text,field_text, contrary_text,section_text = tools_tips_page.check_tools_tips()
        assert button_text == 'You hovered over the Button', 'hover missing or incorrect content'
        assert field_text == 'You hovered over the text field', 'hover missing or incorrect content'
        assert contrary_text == 'You hovered over the Contrary', 'hover missing or incorrect content'
        assert section_text == 'You hovered over the 1.10.32', 'hover missing or incorrect content'



