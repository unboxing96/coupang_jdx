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


# open jdx_2_all_code.py as all_code
with open(
    "/Users/taehyeon/Desktop/jdxcode_0409/selenium/jdx_1-1_all_code.py",
    "r",
    encoding="UTF-8",
) as f:
    all_code = json.load(f)

# get info from code(name, ori_price, sale_price, photo_front, photo_detail)
dic_code = {}
code = ""

cnt_len = len(all_code)
cnt = 1

while cnt <= cnt_len:

    for code, code_num in all_code.items():
        print(code, code_num)
        driver.get(f"https://www.jdx.co.kr/goods/goods_view.php?goodsNo={code_num}")
        time.sleep(1)
        photo_front = []
        i = 1
        name = driver.find_element(By.CLASS_NAME, "item_detail_tit")
        name = name.text[:-13]

        ori_name = name[6:]

        # parsed_ori_name = (
        # ori_name.split()
        # )  # ori_name 파싱 후 parsed_ori_name에 list로 저장

        jdx_name = "6층_JDX_" + ori_name + f"_{code}_평촌점"

        ori_price = driver.find_element(
            By.XPATH, "//*[@id='frmView']/div/div/div[2]/dl[2]/dd/del/span"
        )
        ori_price = ori_price.text
        ori_price = ori_price.replace(",", "")

        sale_price = driver.find_element(
            By.XPATH, "//*[@id='frmView']/div/div/div[2]/dl[1]/dd/strong/strong"
        )
        sale_price = sale_price.text
        sale_price = sale_price.replace(",", "")

        photo_detail = driver.find_element(
            By.XPATH, "//*[@id='detail']/div[2]/div[1]/div[2]/center/img[2]"
        ).get_attribute("src")

        photo_front = []

        n = 1
        while True:
            try:
                d = (
                    driver.find_element(
                        By.XPATH,
                        f"/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div[3]/ul/li[{n}]/a/img",
                    )
                    .get_attribute("src")
                    .replace("t50_", "")
                )
                photo_front.append(d)
                n += 1

            except:
                break

        print(photo_front)

        jdx_name = {"jdx_name": jdx_name}
        ori_name = {"ori_name": ori_name}
        ori_price = {"ori_price": ori_price}
        sale_price = {"sale_price": sale_price}
        photo_front = {"photo_front": photo_front}
        photo_detail = {"photo_detail": photo_detail}

        code_info = [
            jdx_name,
            ori_name,
            ori_price,
            sale_price,
            photo_front,
            photo_detail,
        ]

        dic_code[code] = code_info

        cnt += 1

    driver.close()


with open(
    "/Users/taehyeon/Desktop/jdxcode_0409/selenium/jdx_1-5_info.py",
    "w",
    encoding="utf-8",
) as f:
    json.dump(dic_code, f, ensure_ascii=False, indent=2)


# # assert "Python" in driver.title
# # elem = driver.find_element_by_name("q")
# # elem.clear()
# # elem.send_keys("pycon")
# # elem.send_keys(Keys.RETURN)
# # assert "No results found." not in driver.page_source
# # driver.close()
