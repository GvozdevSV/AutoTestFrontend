import random
import time

from locators.interactions_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators
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
class SelectablePage(BasePage):
    locators = SelectablePageLocators

    def click_selectable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    def select_list_item(self):
        self.element_is_visible(self.locators.TAB_LIST_TITLE).click()
        self.click_selectable_item(self.locators.TAB_LIST)
        active_element = self.element_is_visible(self.locators.TAB_LIST_ACTIVATED)
        return active_element.text

    def select_grid_item(self):
        self.element_is_visible(self.locators.TAB_GRID_TITLE).click()
        self.click_selectable_item(self.locators.GRID_LIST)
        active_element = self.element_is_visible(self.locators.GRID_LIST_ACTIVE)
        return active_element.text
class ResizablePage(BasePage):
    locators = ResizablePageLocators

    def check_resize_box(self):
        input_size = self.element_is_visible(self.locators.OUTPUT_BOX).get_attribute('style')
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_CORNER), random.randint(-300, 400), random.randint(-300, 400))
        output_size = self.element_is_visible(self.locators.OUTPUT_BOX).get_attribute('style')
        return input_size, output_size

    def check_min_max_resize_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_CORNER),-200, -200)
        min_size = self.element_is_present(self.locators.OUTPUT_BOX).get_attribute('style')
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_CORNER), 500, 500)
        max_size = self.element_is_present(self.locators.OUTPUT_BOX).get_attribute('style')
        return min_size, max_size
    def check_resize_free(self):
        input_resize = self.element_is_visible(self.locators.OUTPUT_FREE).get_attribute('style')
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_FREE_CORNER), random.randint(-200, 200), random.randint(-200, 200))
        output_resize = self.element_is_visible(self.locators.OUTPUT_FREE).get_attribute('style')
        return input_resize, output_resize

class DroppablePage(BasePage):
    locators = DroppablePageLocators

    def check_simple_drop(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_me = self.element_is_visible(self.locators.SIMPLE_DRAG)
        drop_to = self.element_is_visible(self.locators.SIMPLE_DROP)
        self.action_drag_and_drop_to_element(drag_me, drop_to)
        return drop_to.text
    def check_accept_drop(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        drag_accept = self.element_is_visible(self.locators.ACCEPT_DRAG)
        drag_no_accept = self.element_is_visible(self.locators.NO_ACCEPT_DRAG)
        drop_to = self.element_is_visible(self.locators.ACCEPT_DROP)
        self.action_drag_and_drop_to_element(drag_no_accept, drop_to)
        no_accept_text = drop_to.text
        self.action_drag_and_drop_to_element(drag_accept, drop_to)
        accept_text = drop_to.text
        return no_accept_text, accept_text

    def check_prevent_drop(self):
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag = self.element_is_visible(self.locators.PREVENT_DRAG)
        greedy_drop = self.element_is_visible(self.locators.GREEDY_DROP_BOX)
        greedy_inner_drop = self.element_is_visible(self.locators.GREEDY_INNER_DROP_BOX)
        no_greedy_drop = self.element_is_visible(self.locators.NOT_GREEDY_DROP_BOX)
        no_greedy_inner_drop = self.element_is_visible(self.locators.NOT_GREEDY_INNER_DROP_BOX)
        self.action_drag_and_drop_to_element(drag, no_greedy_inner_drop)
        no_greedy_text = no_greedy_drop.text
        self.action_drag_and_drop_to_element(drag, greedy_inner_drop)
        greedy_text = greedy_drop.text
        return [no_greedy_text], [greedy_text]
    def check_revers(self):
        self.element_is_visible(self.locators.REVERT_TAB).click()
        revert_drag = self.element_is_visible(self.locators.REVERT_DRAG)
        not_revert_drag = self.element_is_visible(self.locators.NOT_REVERT_DRAG)
        drop = self.element_is_visible(self.locators.DROP_BOX_REVERT)
        self.action_drag_and_drop_by_offset(revert_drag, random.randint(-100, 100), random.randint(-100, 100))
        revert_input_style = revert_drag.get_attribute('style')
        self.action_drag_and_drop_to_element(revert_drag, drop)
        time.sleep(1)
        revert_output_style = revert_drag.get_attribute('style')
        self.action_drag_and_drop_to_element(not_revert_drag, drop)
        not_revert_input_style = not_revert_drag.get_attribute('style')
        self.action_drag_and_drop_by_offset(not_revert_drag, random.randint(-500, -300), random.randint(5, 10))
        time.sleep(1)
        not_revert_output_style = not_revert_drag.get_attribute('style')
        return revert_input_style, revert_output_style, not_revert_input_style, not_revert_output_style
