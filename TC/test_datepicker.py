import datetime

from Base import initialiseDriver, commonMethods
from Pages import datepicker_page
import time

def test_select_current_date():
    browser = initialiseDriver.startBrowser('https://www.way2automation.com/way2auto_jquery/datepicker.php#load_box')
    d = datepicker_page.Date_picker(browser, 'Datepicker')
    c = commonMethods.commonMethods(browser)
    c.switch_to_iframe('iframe_xpath', 'Datepicker')
    d.click_date_button('date_textbox_id')
    d.click_current_date('current_date_xpath')
    getselecteddate = d.text_from_textbox('date_textbox_id')
    today_date = datetime.date.today().strftime('%m/%d/%Y')
    # assert getselecteddate == today_date

def test_verify_user_select_anydate():
    browser = initialiseDriver.startBrowser('https://www.way2automation.com/way2auto_jquery/datepicker.php#load_box')
    d = datepicker_page.Date_picker(browser, 'Datepicker')
    c = commonMethods.commonMethods(browser)
    c.switch_to_iframe('iframe_xpath', 'Datepicker')
    d.click_date_button('date_textbox_id')
    d.click_on_specific_date('25', 'June', 'month_xpath', '2025', 'year_xpath', 'next_button_xpath')
    time.sleep(3)

