from pages.interactions_page import SortablePage, SelectablePage


class TestSortablePage:
    def test_sortable(self, driver):
        sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
        sortable_page.open()
        order_before, order_after = sortable_page.change_list_order()
        grid_before, grid_after =sortable_page.change_grid_order()
        assert order_before != order_after, 'List not changed'
        assert grid_before != grid_after, 'Grid not changed'

class TestSelectablePage:
    def test_selectable(self, driver):
        sortable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
        sortable_page.open()
        item_list = sortable_page.select_list_item()
        item_grid = sortable_page.select_grid_item()
        assert len(item_list) > 0, "No element selected"
        assert len(item_grid) > 0, "No element selected"
