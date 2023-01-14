
"""通用的方法"""
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def wait_element_visible(self,locator,timeout = 20,poll = 0.5):
        """显式等待元素可见
        :return elem
        """
        ele = WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        return ele