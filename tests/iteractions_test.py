from pages.interactions_page import SortablePage


class TestSortablePage:
    def test_sortable(self, driver):
        sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
        sortable_page.open()
        order_before, order_after = sortable_page.change_list_order()
        grid_before, grid_after =sortable_page.change_grid_order()
        assert order_before != order_after, 'List not changed'
        assert grid_before != grid_after, 'Grid not changed'