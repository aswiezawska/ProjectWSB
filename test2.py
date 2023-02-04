import unittest
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver


class MyTestCase(unittest.TestCase):
    invalid_email = "admin@gmail"
    valid_password = "admin123"

    # Setup class and configuration
    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.code2lead.kwad",
            "appActivity": ".MainActivity",
            "automotionName": "UiAutomator2"
        }
        # Start the Appium client
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(20)

    # Close the Appium client
    def tearDown(self):
        self.driver.quit()

        # TC: ID002
        # 1. Open log in menu
        # 2. Enter invalid email
        # 3. Enter password
        # 4. Click on Login button
        # 5. Check if text "Wrong Credentials" is displayed on the screen
        # 6. Check if "username: admin@gmail" is displayed on the screen
        # 7. Check if "password: admin123" is displayed on the screen

    def testID002(self):
        # 1. Open Log in menu and check if element is displayed
        el = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Btn6")
        self.assertTrue(el.is_displayed())
        el.click()
        # 2. Enter invalid email
        email_field = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et4")
        email_field.send_keys(self.invalid_email)
        # 3. Enter password
        password_field = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et5")
        password_field.send_keys(self.valid_password)
        # 4. Click on Login button
        login_button = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Btn3")
        login_button.is_displayed()
        login_button.click()
        # 5. Check if text "Wrong Credentials" is displayed on the screen
        wrong_credentials = self.driver.find_element(AppiumBy.XPATH,
                                                     "*//android.widget.TextView[4][@text = 'Wrong Credentials']")
        wrong_credentials.click()
        self.assertTrue(wrong_credentials.is_displayed())
        # 6. Check if text "username: admin@gmail" is displayed on the screen
        displayed_text = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Tv3")
        displayed_text.click()
        self.assertTrue(displayed_text.is_displayed())
        # 7. Check if text "password: admin123" is displayed on the screen
        displayed_password = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Tv4")
        self.assertTrue(displayed_password.is_displayed())
        displayed_password.click()


if __name__ == '__main__':
    unittest.main()