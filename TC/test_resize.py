from Base import initialiseDriver, commonMethods
from Pages import resize
import time

def test_resize_by_width():
    browser = initialiseDriver.startBrowser('https://www.way2automation.com/way2auto_jquery/resizable.php#load_box')
    r = resize.Resize(browser, 'Resize')
    c = commonMethods.commonMethods(browser)
    c.switch_to_iframe('iframe_resize_xpath', 'Resize')
    beforemoving = c.find_height_and_width_id('resize_box_id', 'Resize', 'width')
    r.resize_area('draggingPoint_xpath')
    aftermoving = c.find_height_and_width_id('resize_box_id', 'Resize', 'width')
    time.sleep(3)
    assert (aftermoving - beforemoving) == 600


