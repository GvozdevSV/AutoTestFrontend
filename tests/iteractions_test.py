from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


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

class TestResizablePage:
    def test_resizeble(self, driver):
        resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
        resizable_page.open()
        min_size, max_size = resizable_page.check_min_max_resize_box()
        input_size, output_size = resizable_page.check_resize_box()
        input_resize, output_resize = resizable_page.check_resize_free()
        assert input_size != output_size, "Size not change"
        assert min_size == 'width: 150px; height: 150px;', "Min size not equal 150 x 150"
        assert max_size == 'width: 500px; height: 300px;', "Max size not equal 500 x 300"
        assert input_resize != output_resize, "Size not change"

