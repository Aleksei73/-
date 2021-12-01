from selenium import webdriver
import pytest
import time
import math
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

link = "https://www.google.com/"
text_search = "Калькулятор"
calc = "1 × 2 - 3 + 1 ="
result = "0"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    search = browser.find_element_by_css_selector('.gLFyf.gsfi').send_keys(text_search,Keys.ENTER)


    num_1 = browser.find_element_by_css_selector('[jsname="N10B9"]').click()
    multi = browser.find_element_by_css_selector('[jsname="YovRWb"]').click()
    num_2 = browser.find_element_by_css_selector('[jsname="lVjWed"]').click()
    minus = browser.find_element_by_css_selector('[jsname="pPHzQc"]').click()
    num_3 = browser.find_element_by_css_selector('[jsname="KN1kY"]').click()
    plus = browser.find_element_by_css_selector('[jsname="XSr6wc"]').click()
    num_01 = browser.find_element_by_css_selector('[jsname="N10B9"]').click()
    equals = browser.find_element_by_css_selector('[jsname="Pt8tGc"]').click()
    check_text = browser.find_element_by_css_selector('[jsname="ubtiRe"]').text
    check_result = browser.find_element_by_css_selector('[jsname="VssY5c"]').text
   
    def test_result():
        assert calc == check_text, "Ошибка в строке памяти"
        assert result == check_result, "Результат не совпадает"
    

finally:
    time.sleep(10)
    browser.quit()