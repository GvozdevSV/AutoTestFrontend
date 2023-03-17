import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertPage


class TestAlertsFrameWindows:
    class TestBrowserWindows:
        def test_new_tab(self, driver):
            test_new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            test_new_tab_page.open()
            new_tab_text = test_new_tab_page.check_opened_new_tab()
            assert new_tab_text == 'This is a sample page'

        def test_new_window(self, driver):
            test_new_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            test_new_window_page.open()
            new_window_text = test_new_window_page.check_opened_new_window()
            assert new_window_text == 'This is a sample page'

    class TestAlerts:
        def test_see_alerts(self, driver):
            test_alert_page = AlertPage(driver, 'https://demoqa.com/alerts')
            test_alert_page.open()
            alert_text = test_alert_page.check_see_alert()
            assert alert_text == 'You clicked a button'

        def test_alerts_after_5_second(self, driver):
            test_alert_page = AlertPage(driver, 'https://demoqa.com/alerts')
            test_alert_page.open()
            alert_text = test_alert_page.check_alert_after_5_second()
            assert alert_text == 'This alert appeared after 5 seconds'

        def test_alerts_confirm(self, driver):
            test_alert_page = AlertPage(driver, 'https://demoqa.com/alerts')
            test_alert_page.open()
            alert_text = test_alert_page.check_confirm_alert()
            assert alert_text == 'You selected Ok'

        def test_alerts_prompt(self, driver):
            test_alert_page = AlertPage(driver, 'https://demoqa.com/alerts')
            test_alert_page.open()
            text_result, text = test_alert_page.check_prompt_alert()
            assert text_result == 'You entered ' + text