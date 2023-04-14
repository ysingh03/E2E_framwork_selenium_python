from Base import initialiseDriver, commonMethods
from Pages import menu_page


def test_verify_menu_hover_data():
    browser = initialiseDriver.startBrowser('https://jqueryui.com/menu/')
    m = menu_page.Menu(browser, 'Menu')
    c = commonMethods.commonMethods(browser)
    c.switch_to_iframe('iframe_xpath', 'Menu')
    check = m.hover_on_menu_element(['Music', 'Rock'], 'Classic')
    assert check == True
