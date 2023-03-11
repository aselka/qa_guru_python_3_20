import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from selene.support.shared import browser
from utils.attach import add_video


@pytest.fixture(scope='function', autouse=True)
def data_search():
    load_dotenv()

    class Settings(BaseModel):
        load_dotenv()
        userName: str = os.getenv('LOGIN')
        accessKey: str = os.getenv('KEY')
        remote_url: str = os.getenv('REMOTE')

    settings = Settings()
    options = UiAutomator2Options().load_capabilities({
        "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",
            'userName': settings.userName,
            'accessKey': settings.accessKey
        }
    })

    browser.config.driver = webdriver.Remote(settings.remote_url, options=options)

    yield

    add_video(browser)
    browser.quit()