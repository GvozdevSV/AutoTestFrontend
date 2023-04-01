
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
class ResizablePageLocators:
    RESIZABLE_BOX_CORNER = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"] span[class="react-resizable-handle react-resizable-handle-se"]')
    OUTPUT_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    RESIZABLE_FREE_CORNER = (By.CSS_SELECTOR, 'div[id="resizable"] span[class="react-resizable-handle react-resizable-handle-se"]')
    OUTPUT_FREE = (By.CSS_SELECTOR, 'div[id="resizable"]')

class DroppablePageLocators:
    #Simple
    SIMPLE_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-simple"]')
    SIMPLE_DRAG = (By.CSS_SELECTOR, 'div[id="simpleDropContainer"] div[class="drag-box mt-4 ui-draggable ui-draggable-handle"]')
    SIMPLE_DROP = (By.CSS_SELECTOR, 'div[id="simpleDropContainer"] div[class="drop-box ui-droppable"]')

    #Accept
    ACCEPT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-accept"]')
    ACCEPT_DRAG = (By.CSS_SELECTOR, 'div[id="acceptDropContainer"] div[id="acceptable"]')
    NO_ACCEPT_DRAG = (By.CSS_SELECTOR, 'div[id="acceptDropContainer"] div[id="notAcceptable"]')
    ACCEPT_DROP = (By.CSS_SELECTOR, 'div[id="acceptDropContainer"] div[class="drop-box ui-droppable"]')

    #Prevent Propogation
    PREVENT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-preventPropogation"]')
    PREVENT_DRAG = (By.CSS_SELECTOR, 'div[id="dragBox"]')
    NOT_GREEDY_DROP_BOX = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"]')
    NOT_GREEDY_INNER_DROP_BOX = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]')
    GREEDY_DROP_BOX = (By.CSS_SELECTOR, 'div[id="greedyDropBox"]')
    GREEDY_INNER_DROP_BOX = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"]')

    #Revert Draggable
    REVERT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-revertable"]')
    REVERT_DRAG = (By.CSS_SELECTOR, 'div[id="revertable"]')
    NOT_REVERT_DRAG = (By.CSS_SELECTOR, 'div[id="notRevertable"]')
    DROP_BOX_REVERT = (By.CSS_SELECTOR, 'div[id="revertableDropContainer"] div[id="droppable"]')