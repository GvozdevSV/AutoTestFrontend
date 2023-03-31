
from selenium.webdriver.common.by import By

class SortablePageLocators:
    TAB_LIST_TITLE = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    TAB_LIST = (By.CSS_SELECTOR, 'div[class="vertical-list-container mt-4"]  div[class="list-group-item list-group-item-action"]')
    TAB_GRID_TITLE = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_LIST = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"]  div[class="list-group-item list-group-item-action"]')
class SelectablePageLocators:
    TAB_LIST_TITLE = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    TAB_LIST = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] li[class="mt-2 list-group-item list-group-item-action"]')
    TAB_LIST_ACTIVATED = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] li[class="mt-2 list-group-item active list-group-item-action"]')
    TAB_GRID_TITLE = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_LIST = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] li[class="list-group-item list-group-item-action"]')
    GRID_LIST_ACTIVE = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] li[class="list-group-item active list-group-item-action"]')