from Base import initialiseDriver, commonMethods
from Pages import selecteditems_page
import time


def test_verify_the_selected_items():
    browser = initialiseDriver.startBrowser('https://jqueryui.com/selectable/')
    c = commonMethods.commonMethods(browser)
    sitem = selecteditems_page.Selected_Item(browser, 'Selectable')
    c.switch_to_iframe('iframe_xpath', 'Selectable')
    sitem.click_item('item1_xpath')
    sitem.press_ctrl_and_click('item2_xpath')
    sitem.press_ctrl_and_click('item3_xpath')
    totalitems = sitem.selected_items('selected_items_xpath')
    assert totalitems == 3



