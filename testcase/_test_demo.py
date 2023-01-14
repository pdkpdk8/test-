import pytest
from selenium import webdriver

def test_goods(driver):
    el3 = driver.find_element_by_id("kw")
    assert el3.tag_name == "input"
    el3.send_keys("goods")
    driver.find_element_by_id("su").click()
    el3.screenshot('3.png')