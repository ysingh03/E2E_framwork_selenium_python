from Base import initialiseDriver, commonMethods
from Pages import drag_page
import time


def test_verify_drag_is_working():
    browser = initialiseDriver.startBrowser('https://www.way2automation.com/way2auto_jquery/draggable.php#load_box')
    d = drag_page.Drag(browser, 'Drag')
    c = commonMethods.commonMethods(browser)
    c.switch_to_iframe('iframe1_xpath', 'Drag')
    beforeDragPosition = d.find_height_and_width_xpath('drag_box_id')
    d.drag_and_drop('drag_box_id')
    afterDragPosition = d.find_height_and_width_xpath('drag_box_id')
    time.sleep(3)
    assert afterDragPosition != beforeDragPosition


def test_verify_drag_is_working1():
    browser = initialiseDriver.startBrowser('https://www.way2automation.com/way2auto_jquery/draggable.php#load_box')
    d = drag_page.Drag(browser, 'Drag')
    d.click_Cursor_style_page()
    c = commonMethods.commonMethods(browser)
    c.switch_to_iframe('iframe3_xpath', 'Drag')
    beforeDragPosition = d.current_position_of_element('drag_box_id3')
    time.sleep(3)
    d.drag_and_drop('drag_box_id3')
    afterDragPosition = d.current_position_of_element('drag_box_id3')
    time.sleep(3)


def test_verify_drop_on_destination():
    browser = initialiseDriver.startBrowser('https://www.way2automation.com/way2auto_jquery/droppable.php#load_box')
    d = drag_page.Drag(browser, 'Drag')
    c = commonMethods.commonMethods(browser)
    c.switch_to_iframe('iframe2_xpath', 'Drag')
    d.drag_and_drop_to_destination('drag_box_id', 'drop_box_id')
    expected = c.verify_element_is_visible('highlight_value_xpath', 'Drag')
    assert expected == True
