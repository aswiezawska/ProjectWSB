import unittest
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver


class MyTestCase(unittest.TestCase):
    enter_value = "hello world!"

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
        # 1. On my page: check if my page is loaded
        # 2. Click on "Enter some value" field
        # 3. Enter "hello world" in the "Enter some value" button
        # 4. Click "Submit" button
        # 5. Check if values "hello world" are displayed

    def testID003(self):
        # 1. On my page: check if my page is loaded
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Appium Demo']").is_displayed()
        # 2. Click on "Enter some value" field
        el = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.assertTrue(el.is_displayed())
        el.click()
        # 3. Enter "hello world" in the "Enter some value" button
        field = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
        field.send_keys("hello world!")
        # 4. Click "Submit" button
        button = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Btn1")
        self.assertTrue(button.is_displayed())
        button.click()
        # 5. Check if values "hello world" are displayed
        hello1 = self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.code2lead.kwad:id/Et1']")
        self.assertTrue(hello1.is_displayed())
        hello2 = self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Tv1")
        self.assertTrue(hello2.is_displayed())


if __name__ == '__main__':
    unittest.main()