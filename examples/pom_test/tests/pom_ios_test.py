import pytest
import time
import json

from examples.pom_test.pages.iosPage import IosPage
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


with open("test_settings.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

    cloudUser = jsonObject['CLOUD']['momentum.user']
    cloudToken = jsonObject['CLOUD']['momentum.token']
    cloudHost = jsonObject['CLOUD']['momentum.host']
    cloudIosApp = jsonObject['CLOUD']['ios']['momentum.app']
    cloudIosDeviceName = jsonObject['CLOUD']['ios']['momentum.deviceList'][0]
    print(cloudHost)

desired_caps = {
    "platformName": "ios",
    "appium:automationName": "XCUITest",
    "momentum:user": cloudUser,
    "momentum:token": cloudToken,
    "momentum:gw": cloudIosDeviceName,
    "appium:app": cloudIosApp,
    "appium:autoGrantPermissions": True,
    "appium:language": "en",
    "appium:locale": "en",
    "appium:fullReset": True,
    "appium:noReset": False,
    "appium:deviceName": "",
    "appium:udid": ""
}

class TestPageObjectModel():

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Remote(cloudHost, desired_caps)
        driver.implicitly_wait(8)

        yield
        driver.quit()

    def test_pom(self, test_setup):
       IosPage.myFunction(driver)