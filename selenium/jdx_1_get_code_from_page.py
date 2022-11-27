from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import json
import os

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

# get all code from jdx (if num == LAST PAGE + 1: break)
all_code = {}

# change page_num (should be <= 15) (last page + 1)
num = 1  # start page
endpage_num = 10

e_list = []
c_list = []

while True:
    if num == endpage_num:
        break
    driver.get(f"https://www.jdx.co.kr/goods/goods_list.php?page={num}&cateCd=002")
    time.sleep(1)
    codes = driver.find_elements(By.CLASS_NAME, "item_name")
    elems_parent = driver.find_elements(By.CLASS_NAME, "item_photo_box")

    for elem_parent in elems_parent:
        elem = elem_parent.find_element(By.TAG_NAME, "a")
        e_list.append(elem.get_attribute("href")[-10:])

    for code in codes:
        c = code.text[-12:-1]
        c_list.append(c)

    for i in range(len(c_list)):
        all_code[c_list[i]] = e_list[i]

    num += 1

# save all_code to py
with open(
    "/Users/taehyeon/Desktop/jdxcode_0409/selenium/jdx_1-1_all_code.py", "w"
) as f:
    json.dump(all_code, f, ensure_ascii=False, indent=2)

driver.close()


##########################################################################################################

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# import json
