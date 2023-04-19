import time

from Base import initialiseDriver, commonMethods
from Pages import alert_page
from selenium import webdriver
webdriver.Chrome()

def test_verify_simple_alert_accept():
    browser = initialiseDriver.startBrowser('https://www.way2automation.com/way2auto_jquery/alert.php#load_box')
    c = commonMethods.commonMethods(browser)
    a = alert_page.Alerts(browser, 'Alerts')
    c.switch_to_iframe('iframe_xpath', 'Alerts')
    a.click_button('click_simple_alertbox_xpath')
    a.click_simple_alert_box()

def test_verify_input_alert_accept():
    browser = initialiseDriver.startBrowser('https://www.way2automation.com/way2auto_jquery/alert.php#load_box')
    c = commonMethods.commonMethods(browser)
    a = alert_page.Alerts(browser, 'Alerts')
    a.click_button('input_section_xpath')
    c.switch_to_iframe('iframe1_xpath', 'Alerts')
    a.click_button('click_inputbox_xpath')
    time.sleep(3)
    a.click_input_alert_box()
    time.sleep(3)
    c.switch_to_iframe('iframe1_xpath', 'Alerts')
    a.click_button('click_inputbox_xpath')
    a.dismiss_alert_box()
    time.sleep(3)
