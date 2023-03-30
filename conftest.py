import datetime
import logging

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="192.168.0.103")
    parser.addoption("--url", default="http://192.168.0.103:8081")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--video", action="store_true")
    parser.addoption("--bv")
    parser.addoption("--log_level", action="store", default="DEBUG")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    video = request.config.getoption("--video")
    log_level = request.config.getoption("--log_level")

    if executor == "local":
        caps = {'goog:chromeOptions': {}}
        driver = webdriver.Chrome(desired_capabilities=caps)

    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        caps = {
            "browserName": browser,
            # "platformName": "Windows 7"
            # "browserVersion": version,
            # "screenResolution": "1280x720",
            # "selenoid:options": {
            #     "enableVNC": vnc,
            #     "enableVideo": video,
            #     "enableLog": logs
            # },
            # 'goog:chromeOptions': {}
        }

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps,
        )

    def finalizer():
        driver.quit()

    request.addfinalizer(finalizer)
    return driver


@pytest.fixture
def url(request):
    return request.config.getoption('--url')
