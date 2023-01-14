import pytest
from selenium import webdriver
import time
import logging
import allure

logger = logging.getLogger(__name__)

@pytest.fixture(scope='module')
def driver():
    chrome_driver = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe' #chrome_driver 存放位置
    driver = webdriver.Chrome(executable_path=chrome_driver)
    driver.get("https://login.taobao.com/member/login.jhtml?spm=a21bo.jianhua.754894437.1.5af911d96I0gom&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F")
    print("请扫码登录")
    time.sleep(5)
    yield driver #测试用例之后去执行的命令
    driver.quit()

@pytest.fixture(scope='module')
def address(driver):
    driver.get("https://member1.taobao.com/member/fresh/deliver_address.htm?spm=a1z02.1.972272805.d4912033.3dzM8p")
    time.sleep(3)
    yield driver #测试用例之后去执行的命令
    driver.quit()

#创建钩子
def pytest_runtest_setup(item):
    logger.info(f'开始执行：{item.nodeid}'.center(60,'-'))

def pytest_runtest_teardown(item):
    logger.info(f'执行结束：{item.nodeid}'.center(60,'-'))

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    path = f"images/{time.time()}.png"

    if report.when == "call":
        o = report.outcome
        s = f"用例执行结果：【{report.outcome}】"
        if o == "failed":
            logger.error(s)
        elif o == "skip":
            logger.warning(s)
        else:
            logger.info(s)
        
        if "driver" in item.fixturenames:
            driver = item.funcargs['driver']
            # driver.get_screenshot_as_file(path)

            # logger.info(f"页面截图：{path}")
            allure.attach(driver.get_screenshot_as_png(),'页面截图')