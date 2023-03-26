import random

from locators.interactions_locators import SortablePageLocators
from pages.base_page import BasePage

class SortablePage(BasePage):
    locators = SortablePageLocators

    def get_sortable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self):
        self.element_is_visible(self.locators.TAB_LIST_TITLE).click()
        order_before = self.get_sortable_item(self.locators.TAB_LIST)
        item_list = random.sample(self.elements_are_visible(self.locators.TAB_LIST), k=2) #выбираем 2 случайных элемента
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_item(self.locators.TAB_LIST)
        return order_before, order_after

    def change_grid_order(self):
        self.element_is_visible(self.locators.TAB_GRID_TITLE).click()
        order_before = self.get_sortable_item(self.locators.GRID_LIST)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_LIST), k=2) #выбираем 2 случайных элемента
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_item(self.locators.GRID_LIST)
        return order_before, order_after