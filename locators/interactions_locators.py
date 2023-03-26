
from selenium.webdriver.common.by import By

class SortablePageLocators:
    TAB_LIST_TITLE = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    TAB_LIST = (By.CSS_SELECTOR, 'div[class="vertical-list-container mt-4"]  div[class="list-group-item list-group-item-action"]')
    TAB_GRID_TITLE = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_LIST = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"]  div[class="list-group-item list-group-item-action"]')
