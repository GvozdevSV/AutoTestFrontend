import time


from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertPage, FramePage, NestedFramesPage, ModalDialogsPage


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

    class TestFrames:
        def test_frames(self, driver):
            test_frames_page = FramePage(driver, 'https://demoqa.com/frames')
            test_frames_page.open()
            result_frame1 = test_frames_page.check_frame('frame1')
            result_frame2 = test_frames_page.check_frame('frame2')
            assert result_frame1 == ('This is a sample page', '500px', '350px')
            assert result_frame2 == ('This is a sample page', '100px', '100px')

    class TestNestedFrames:
        def test_nested_frames(self, driver):
            test_nested_frames_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            test_nested_frames_page.open()
            parents_result = test_nested_frames_page.check_nested_frames('parents_frame')
            child_result = test_nested_frames_page.check_nested_frames('child_frame')
            assert parents_result == ('Parent frame', '500px', '350px')
            assert child_result == 'Child Iframe'

    class TestModalDialogs:
        def test_modal_dialogs_open_get_title_close(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            small_modal_title, large_modal_title = modal_dialogs_page.open_get_title_close()
            assert small_modal_title == 'Small Modal'
            assert large_modal_title == 'Large Modal'






