import allure
import moment
import pytest
import os

from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from Utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()


    def test_logout(self):

        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            assert x == "abc"
        except AssertionError as error:
            print("it was an Assertion error")
            print(error)
            captureTime = moment.now().strftime("%H-%M-%S_%D-%M-%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + captureTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("./Users/yatin/Desktop/AutomationFramework_1/Screenshots/ "+screenshotName+".png")
            driver.save_screenshot("/Users/yatin/Desktop/AutomationFramework_1/Screenshots/ "+screenshotName+".png")
            raise
        except:
            print("unable to go to homepage")
            captureTime = moment.now().strftime("%H-%M-%S_%D-%M-%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + captureTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yatin/Desktop/AutomationFramework_1/Screenshots/" + screenshotName + ".png")
            raise
        else:
            print("NO exceptions")
        finally:
            print("i am inside finally block")
