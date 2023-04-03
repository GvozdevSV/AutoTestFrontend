import allure

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage
@allure.suite('TestInteractions')
class TestInteractions:
    @allure.feature('Sortable Page')
    class TestSortablePage:
        @allure.title('проверка перемешивания объектов')
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_before, order_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert order_before != order_after, 'List not changed'
            assert grid_before != grid_after, 'Grid not changed'

    @allure.feature('Selectable Page')
    class TestSelectablePage:
        @allure.title('проверка выбора объекта из списка и таблицы')
        def test_selectable(self, driver):
            sortable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            sortable_page.open()
            item_list = sortable_page.select_list_item()
            item_grid = sortable_page.select_grid_item()
            assert len(item_list) > 0, "No element selected"
            assert len(item_grid) > 0, "No element selected"

    @allure.feature('Resizable Page')
    class TestResizablePage:
        @allure.title('проверка изменения размеров окон')
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

    @allure.feature('Droppable Page')
    class TestDroppablePage:
        @allure.title('проверка перетаскиваемых объектов')
        def test_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            simple_drop = droppable_page.check_simple_drop()
            no_accept, accept = droppable_page.check_accept_drop()
            no_greedy, greedy = droppable_page.check_prevent_drop()
            revert_input, revert_output, not_revert_input, not_revert_output = droppable_page.check_revers()
            assert simple_drop == "Dropped!", "Object not dropped"
            assert no_accept == "Drop here", "Object dropped"
            assert accept == "Dropped!", "Object not dropped"
            assert no_greedy == ['Dropped!\nDropped!'], "No greedy object not dropped"
            assert greedy == ['Outer droppable\nDropped!'], "Greedy object not dropped"
            assert revert_input == revert_output, "Object not revert"
            assert not_revert_input == not_revert_output, "Object not revert"



