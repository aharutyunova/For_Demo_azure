from selenium import webdriver
import pytest
import logging
import os
from datetime import datetime
import allure


@pytest.fixture
def get_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    filemode='w'
)


@pytest.fixture()
def test_logger(request):
    today_date = datetime.today().date()
    os.makedirs(f"logs_{today_date}", exist_ok=True)
    test_name = request.node.name
    log_path = os.path.join(f"logs_{today_date}", test_name)
    logger = logging.getLogger(test_name)
    file_handler = logging.FileHandler(log_path, mode='w')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    logger.info(f'{test_name} is started')
    yield logger
    logger.info(f'{test_name} is finished')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call":
        if result.outcome == 'failed':
            allure.attach(
                item.funcargs.get("get_driver").get_screenshot_as_png(),
                name=f"{item.name}_screen",
                attachment_type=allure.attachment_type.PNG)