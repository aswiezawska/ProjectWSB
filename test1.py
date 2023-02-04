import unittest
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver



class MyTestCase(unittest.TestCase):

    valid_email = "admin@gmail.com"
    valid_password = "admin123"
    enter_admin = "Ania"

    # Setup class and configuration
    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.code2lead.kwad",
            "appActivity": ".MainActivity" ,
            "automotionName": "UiAutomator2"
        }
        # Start the Appium client
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(20)

    # Close the Appium client
    def tearDown(self):
        self.driver.quit()

        #TC: ID001
        # 1. Open log in menu
        # 2. Enter valid email
        # 3. Enter password
        # 4. Click on Login button
        # 5. Enter Admin
        # 6. Click submit button

    def testID001(self):
        # 1. Open Log in menu
        el = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Btn6")
        # Check if element is displayed
        self.assertTrue(el.is_displayed())
        el.click()
        # 2. Enter valid email
        email_field = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et4")
        email_field.send_keys(self.valid_email)
        # 3. Enter password
        password_field = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et5")
        password_field.send_keys(self.valid_password)
        # 4. Click on Login button
        login_button = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Btn3")
        login_button.is_displayed()
        login_button.click()
        # 5. Enter Admin
        _enter_admin = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Edt_admin")
        _enter_admin.send_keys(self.enter_admin)
        # 6. Click submit button
        submit_button = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Btn_admin_sub")
        submit_button.is_displayed()
        submit_button.click()



if __name__ == '__main__':
    unittest.main()