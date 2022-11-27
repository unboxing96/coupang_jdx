##########test real

import os
import sys
import time
from time import strftime, gmtime
import hmac
import hashlib
import urllib.parse
import urllib.request
import ssl
import json
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import pyautogui

# ********************************************************#
import json

with open(
    "/Users/taehyeon/Desktop/jdxcode_0409/selenium/jdx_3-3_result.py",
    "r",
    encoding="utf-8",
) as f:
    all_data = json.load(f)

with open(
    "/Users/taehyeon/Desktop/jdxcode_0409/selenium/jdx_3-2_metadata.py",
    "r",
    encoding="utf-8",
) as ff:
    metadata = json.load(ff)

fin = 1
err_code = []
all_code = list(all_data.keys())
for code in all_code:
    code_dict = all_data[f"{code}"]
    displayCategoryCode = code_dict["displayCategoryCode"]  # str
    sellerProductName = code_dict["sellerProductName"]  # str
    displayProductName = code_dict["displayProductName"]  # str
    generalProductName = code_dict["generalProductName"]  # str
    originalPrice = int(code_dict["originalPrice"])  # str
    salePrice = int(code_dict["salePrice"])  # str
    attributeTypeName_size = code_dict["attributeTypeName_size"]  # list
    attributeTypeName_color = code_dict["attributeTypeName_color"]  # str
    imageType_REPRESENTATION = code_dict["imageType_REPRESENTATION"]  # list
    imageType_DETAIL = code_dict["imageType_DETAIL"]  # str

    # ****************************************************************************************************************#

    notice_val = [
        {
            "noticeCategoryName": "의류",
            "noticeCategoryDetailName": "제품 소재",
            "content": "상세페이지 참조",
        },
        {
            "noticeCategoryName": "의류",
            "noticeCategoryDetailName": "색상",
            "content": "상세페이지 참조",
        },
        {
            "noticeCategoryName": "의류",
            "noticeCategoryDetailName": "치수",
            "content": "상세페이지 참조",
        },
        {
            "noticeCategoryName": "의류",
            "noticeCategoryDetailName": "제조자(수입자)",
            "content": "상세페이지 참조",
        },
        {
            "noticeCategoryName": "의류",
            "noticeCategoryDetailName": "제조국",
            "content": "상세페이지 참조",
        },
        {
            "noticeCategoryName": "의류",
            "noticeCategoryDetailName": "세탁방법 및 취급시 주의사항",
            "content": "상세페이지 참조",
        },
        {
            "noticeCategoryName": "의류",
            "noticeCategoryDetailName": "제조연월",
            "content": "상세페이지 참조",
        },
        {
            "noticeCategoryName": "의류",
            "noticeCategoryDetailName": "품질보증기준",
            "content": "상세페이지 참조",
        },
        {
            "noticeCategoryName": "의류",
            "noticeCategoryDetailName": "A/S 책임자와 전화번호",
            "content": "031-380-1451",
        },
    ]

    ################################################################################################

    img_val = []
    img_val.append(
        {
            "imageOrder": 0,
            "imageType": "REPRESENTATION",
            "vendorPath": f"{imageType_REPRESENTATION[0]}",
        }
    )

    i = 1
    for front_photo in imageType_REPRESENTATION[1:]:
        img = {}
        img["imageOrder"] = i
        img["imageType"] = "DETAIL"
        img["vendorPath"] = front_photo
        img_val.append(img)
        i += 1

    ################################################################################################

    item_val = []

    for size in attributeTypeName_size:
        item_info = {
            "itemName": f"{attributeTypeName_color} {size}",
            "originalPrice": originalPrice,
            "salePrice": salePrice,
            "maximumBuyCount": 30,
            "maximumBuyForPerson": 30,
            "outboundShippingTimeDay": 4,
            "maximumBuyForPersonPeriod": 1,
            "unitCount": 1,
            "adultOnly": "EVERYONE",
            "taxType": "TAX",
            "parallelImported": "NOT_PARALLEL_IMPORTED",
            "overseasPurchased": "NOT_OVERSEAS_PURCHASED",
            "pccNeeded": "false",
            # "externalVendorSku": "A00138689",
            # "barcode": "",
            # "emptyBarcode": true,
            # "emptyBarcodeReason": "상품확인불가_바코드없음사유",
            # "modelNo": "1717171",
            # "extraProperties": null,
            # "certifications": [
            #   {
            # 	"certificationType": "NOT_REQUIRED",
            # 	"certificationCode": ""
            #   }
            # ],
            "searchTags": [
                "jdx",
                "JDX",
                "jdx 평촌점",
                "jdx 남성",
                "jdx 여성",
                "jdx 골프웨어 남성",
                "jdx 골프웨어 여성",
                "jdx 골프 웨어",
                "남성 골프 웨어",
                "여성 골프 웨어",
                "골프 웨어 이월상품",
                "골프 웨어",
                "골프 바지",
                "골프 티셔츠",
                "골프 점퍼",
                "골프화",
                "남성 스포츠웨어",
                "여성 스포츠웨어",
                "웨스트우드 이월상품",
            ],
            "images": img_val,
            "notices": notice_val,
            "attributes": [
                {"attributeTypeName": "패션의류/잡화 사이즈", "attributeValueName": f"{size}"},
                {
                    "attributeTypeName": "색상",
                    "attributeValueName": f"{attributeTypeName_color}",
                },
            ],
            "contents": [
                {
                    "contentsType": "IMAGE",
                    "contentDetails": [
                        {
                            "content": "https://i.esdrop.com/d/Li2uh5FG5E.png",
                            "detailType": "IMAGE",
                        },
                        {
                            "content": "https://i.esdrop.com/d/f/HV29DjMTCH/M2OpXLFHkc.jpg",
                            "detailType": "IMAGE",
                        },
                        {"content": imageType_DETAIL, "detailType": "IMAGE"},
                    ],
                }
            ]
            # "offerCondition": "NEW",
            # "offerDescription": ""
        }
        item_val.append(item_info)

    # ****************************************************************************************************************#
    # os.environ['TZ'] = 'GMT+0'
    # datetime=time.strftime('%y%m%d')+'T'+time.strftime('%H%M%S')+'Z'

    dateGMT = strftime("%y%m%d", gmtime())
    timeGMT = strftime("%H%M%S", gmtime())
    datetime = dateGMT + "T" + timeGMT + "Z"

    method = "POST"
    path = "/v2/providers/seller_api/apis/api/v1/marketplace/seller-products"
    message = datetime + method + path

    # replace with your own accesskey
    accesskey = "8d837660-c380-4673-83f9-b1a5d5b4fbba"
    # replace with your own secretKey
    secretkey = "b5c9176c28a82fda9dc26669f16f196ce9350a2f"

    # ********************************************************#
    # authorize, demonstrate how to generate hmac signature here
    signature = hmac.new(
        secretkey.encode("utf-8"), message.encode("utf-8"), hashlib.sha256
    ).hexdigest()
    authorization = (
        "CEA algorithm=HmacSHA256, access-key="
        + accesskey
        + ", signed-date="
        + datetime
        + ", signature="
        + signature
    )
    # print out the hmac key
    # print(authorization)
    # ********************************************************#

    # ************* SEND THE REQUEST *************
    url = "https://api-gateway.coupang.com" + path

    true = True
    false = False
    null = None
    strjson = {
        "displayCategoryCode": displayCategoryCode,
        "sellerProductName": f"{sellerProductName}",
        "vendorId": "A00138689",
        #########################################################################Change Date!!
        "saleStartedAt": "2020-12-18T20:20:00",
        "saleEndedAt": "2099-12-31T23:59:59",
        "displayProductName": f"{displayProductName}",
        "brand": "JDX_",
        "generalProductName": f"{generalProductName}",
        # "productGroup": "클렌징 오일",
        "deliveryMethod": "SEQUENCIAL",
        "deliveryCompanyCode": "HYUNDAI",
        "deliveryChargeType": "CONDITIONAL_FREE",
        "deliveryCharge": 2500,
        "freeShipOverAmount": 30000,
        "deliveryChargeOnReturn": 2500,
        "remoteAreaDeliverable": "N",
        "unionDeliveryType": "UNION_DELIVERY",
        "returnCenterCode": "1000517251",
        "returnChargeName": "경기도 안양시 동안로 119 뉴코아아울렛 평촌점 9층 온라인사무실",
        "companyContactNumber": "031-380-1451",
        "returnZipCode": "14073",
        "returnAddress": "경기도 안양시 동안구 동안로 119 (호계동)",
        "returnAddressDetail": "뉴코아아울렛 평촌점 9층 온라인 사무실_4",
        "returnCharge": 2500,
        # "returnChargeVendor": "N",
        # "afterServiceInformation": "A/S안내 1544-1255",
        # "afterServiceContactNumber": "1544-1255",
        "outboundShippingPlaceCode": 1790006,
        "vendorUserId": "aa4151",
        "requested": false,
        "items": item_val,
        "extraInfoMessage": "",
        "manufacture": "(주)신한코리아",
    }

    data = json.dumps(strjson).encode("utf-8")

    print("BEGIN REQUEST++++++++++++++++++++++++++++++++++++")
    req = urllib.request.Request(url)

    req.add_header("Content-type", "application/json;charset=UTF-8")
    req.add_header("Authorization", authorization)

    req.get_method = lambda: method

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    print("RESPONSE++++++++++++++++++++++++++++++++++++")
    try:
        resp = urllib.request.urlopen(req, data, context=ctx)
    except urllib.request.HTTPError as e:
        print(e.code)
        print(e.reason)
        print(e.fp.read())
        err_code.append(code)
        print(code)
    except urllib.request.URLError as e:
        print(e.errno)
        print(e.reason)
        print(e.fp.read())
        err_code.append(code)
        print(code)
    else:
        # 200
        body = resp.read().decode(resp.headers.get_content_charset())
        print(body)
        print(fin)
        fin += 1
    time.sleep(0.3)
print(err_code)


# 	# # ****************************************************************************************************************
# 	# #selenium detail image upload
# 	time.sleep(3)
# 	body_code = body[-12:-1]

# 	driver = webdriver.Chrome(r"C:\Users\bel03\OneDrive\바탕 화면\WORK\coupang\jdx\chromedriver.exe")
# 	driver.get(f"https://wing.coupang.com/tenants/seller-web/vendor-inventory/modify?vendorInventoryId={body_code}&searchIds=&startTime=2000-01-01&endTime=2099-12-31&productName=&brandName=&manufacturerName=&productType=&dateType=productRegistrationDate&dateRangeShowStyle=true&dateRange=all&saleEndDatePeriodType=&includeUsedProduct=&deleteType=false&deliveryMethod=&shippingType=&shipping=&otherType=&productStatus=SAVED,WAIT_FOR_SALE,SOLD_OUT,END_FOR_SALE,APPROVING,IN_REVIEW,DENIED,APPROVED&advanceConditionShow=false&displayCategoryCodes=&currentMenuCode=&page=1&countPerPage=50&sortField=vendorInventoryId&desc=true&fromListV2=true")
# 	elem_id = driver.find_element_by_id("userID")
# 	elem_id.send_keys("aa4151")
# 	elem_pw = driver.find_element_by_id("userPWD")
# 	elem_pw.send_keys("kk8929$$")
# 	elem_pw.send_keys(Keys.RETURN)
# 	time.sleep(2)

# 	# checkB = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div/div[3]/table/thead/tr/th[1]/span/input")
# 	# checkB.send_keys(webdriver.common.keys.Keys.SPACE)

# 	modifyB = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/button")
# 	modifyB.send_keys(webdriver.common.keys.Keys.RETURN)

# 	for i in range(magic_num):
# 		try:
# 			add_img = EC.presence_of_element_located((By.XPATH, "//*[@id='panel-contents']/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/button[1]"))  # Example xpath2
# 			WebDriverWait(driver, 10).until(add_img).click() # This opens the windows file selector
# 			time.sleep(1)
# 			pyautogui.write(f"C:\\jdximg\\new{i+1}.png", interval=0.1)
# 			pyautogui.press('return')
# 			time.sleep(1)
# 		except:
# 			errorB = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[6]/button[2]")
# 			errorB.send_keys(webdriver.common.keys.Keys.RETURN)
# 			err_code.append(code)
# 			print(code)

# 	# WebDriverWait(driver, 10).until(add_img).click() # This opens the windows file sel
# 	# time.sleep(1)
# 	# pyautogui.write(f"C:\\jdximg\\333.png", interval=0.1)
# 	# pyautogui.press('return')

# 	button = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/button[2]")
# 	driver.implicitly_wait(10)
# 	ActionChains(driver).move_to_element(button).click(button).perform()

# 	# save1 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/button[2]")
# 	# save1.send_keys(webdriver.common.keys.Keys.RETURN)

# 	saveB = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/footer/div/div/div[2]/button[1]")
# 	saveB.send_keys(webdriver.common.keys.Keys.RETURN)

# 	driver.close()
# 	print(fin)
# 	fin += 1

# 	break

# print(err_code)
