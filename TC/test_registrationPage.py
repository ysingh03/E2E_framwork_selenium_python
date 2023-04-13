import time

from Base import initialiseDriver
from Pages import registrationPage


def test_verifyRegistration():
    browser = initialiseDriver.startBrowser("https://www.way2automation.com/way2auto_jquery/registration.php#load_box")
    r = registrationPage.reg(browser, "Registration")
    r.enter_Data_Using_Xpath("firstname_xpath", "Yogesh")
    r.enter_Data_Using_Xpath("lastname_xpath", 'Kumar')
    time.sleep(3)
    r.click_element("maritalstatus_xpath")
    r.click_element("hobby_xpath")
    r.select_Item_In_Dropdown("country_xpath", "India")
    r.select_Item_In_Dropdown("dobmonth_xpath", "1")
    r.select_Item_In_Dropdown("dobday_xpath", "1")
    r.select_Item_In_Dropdown("dobyear_xpath", "2014")
    r.enter_Data_Using_Name("phoneno_name", "12345678")
    r.enter_Data_Using_Name("username_name", "abc123")
    r.enter_Data_Using_Name("email_name", "abc@abc.in")
    time.sleep(3)

    upload_data_path = "F:\Testing\Selenium_Projects\E2E_framwork_selenium_python\ConfigData\Python.pdf"
    r.enter_Data_Using_Xpath("file_xpath", upload_data_path)
    r.enter_Data_Using_Tagname("about_tagname", "This is my name yogi")
    time.sleep(3)
    r.enter_Data_Using_Name("pwd_name", "12345")
    r.enter_Data_Using_Name("c_pwd_name", "12345")
    r.click_element("submit_xpath")
    time.sleep(3)
