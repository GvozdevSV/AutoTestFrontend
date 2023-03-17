import time

from pages.alerts_frame_windows_page import BrowserWindowsPage


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
