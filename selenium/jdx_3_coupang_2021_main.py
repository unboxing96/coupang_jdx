#-*- coding: utf-8 -*-
import json 

# with open("C:\\Users\\bel03\OneDrive\\바탕 화면\\WORK\\coupang\\jdx\\jdx_all_code.txt", "r") as ff:
#     codes = json.load(ff)
#     for code in codes:
#         print(code)
#         break
# with open("C:\\Users\\bel03\OneDrive\\바탕 화면\\WORK\\coupang\\jdx\\jdx_category_real.py", "r") as f:
#     data = json.load(f)
#     # print(type(data))
#     # print(data["M"]["TL"]) 

# data_M = data["M"]
# data_W = data["W"]
# displayCategoryCode = []

# for code in codes:
#     if code[6] == "M":
#         data = data_M
#     else:
#         data = data_W
    
#     if code[4:6] in list(data.keys()):
#         pro_code = code[4:6]
#         displayCategoryCode = data[pro_code]
#         category_num_list.append(category_num)

# with open("C:\\Users\\bel03\OneDrive\\바탕 화면\\WORK\\coupang\\jdx\\jdx_displayCategoryCode.py", "w") as fff:
#     json.dump(displayCategoryCode, fff)


##############start#################

#get category num from jdx code
with open("./jdx_1-3_category_num_by_code.py", "r", encoding="utf-8") as ff:
    data = json.load(ff)


data_M = data["M"]
data_W = data["W"]
data_C = data["color_code"]

displayCategoryCode = []

i = 1

#get jdx info
with open("./jdx_2-1_result_easy_name.py", "r", encoding="utf-8") as f:
    codes = json.load(f)

final_jdx_result = {}

for code in codes:
    jdx_result = {}
    
    #################################   get size & CategoryCode    ############################ 
    # man_code = ["1", "2", "3", "4", "9"]
    if code[6] == "M":
        if code[4] == "P":
            attributeTypeName_size = ["78(31)", "82(32)", "84(33)", "86(34)", "88(35)", "92(37)"]
        elif code[4] == "T" or code[4] == "S" or code[4] == "W":
            attributeTypeName_size = [95, 100, 105, 110]
        elif code[4:6] == "AT":
            attributeTypeName_size = [255, 260, 265, 270, 275]
        elif code[4:6] == "AB" or code[4:6] == "AP":
            attributeTypeName_size = [95, 100, 105]
        else:
            attributeTypeName_size = ["FREE"]
        
        if code[4:6] in list(data_M.keys()):
            pro_code = code[4:6]
            displayCategoryCode = data_M[pro_code]
    

    else:
        if code[4] == "P":
            attributeTypeName_size = ["64(26)", "67(27)", "70(28)", "73(29)", "76(30)"]
        elif code[4] == "T" or code[4] == "S" or code[4] == "W":
            attributeTypeName_size = [90, 95, 100, 105]
        elif code[4:6] == "AT":
            attributeTypeName_size = [230, 235, 240, 245, 250]
        elif code[4:6] == "AA":
            attributeTypeName_size = ["75A", "75B", "80A", "80B", "85A", "85B"]
        elif code[4:6] == "AP":
            attributeTypeName_size = [90, 95, 100]
        else:
            attributeTypeName_size = ["FREE"]
        
        if code[4:6] in list(data_W.keys()):
            pro_code = code[4:6]
            displayCategoryCode = data_W[pro_code]

    # get color
    if code[-2:] in list(data_C.keys()):
        color_code = code[-2:]
        attributeTypeName_color = data_C[color_code]
    else:
        attributeTypeName_color = "단일색상"




    ###############################     get info to coupang.api setting     ###############################

    jdx_name = codes[code][0]['jdx_name']
    ori_name = codes[code][1]['ori_name']
    parsed_ori_name = codes[code][2]['parsed_ori_name']
    ori = codes[code][3]['ori_price']
    sale = codes[code][4]['sale_price']
    photo_f = codes[code][5]['photo_front']
    photo_d = codes[code][6]['photo_detail']
    new_name = codes[code][7]["new_name"]


    #name to easy name <----------------------------------------------------작업 대상
    #여기서 파싱 사전 호출, 하나씩 대체 후, 순서에 맞게 저장, 새로운 변수 만듦
    #if code[ : ]가 ~~라면 new_name.append

    sellerProductName = "6층_JDX_" + new_name + f"_{code}" + "_평촌점"
    displayProductName = "JDX_" + new_name + "_평촌점"
    generalProductName = new_name
    originalPrice = ori
    salePrice = sale
    imageType_REPRESENTATION = photo_f
    imageType_DETAIL = photo_d



    #name & price & image
    #jdx_result["originalName"] = originalName #아카이빙용. 쿠팡 노출X <----------------------------------------------------작업 대상
    jdx_result["sellerProductName"] = sellerProductName
    jdx_result["displayProductName"] = displayProductName
    jdx_result["generalProductName"] = generalProductName
    jdx_result["originalPrice"] = originalPrice
    jdx_result["salePrice"] = salePrice
    jdx_result["imageType_REPRESENTATION"] = imageType_REPRESENTATION
    jdx_result["imageType_DETAIL"] = imageType_DETAIL

    #category & size & color
    jdx_result["displayCategoryCode"] = displayCategoryCode
    jdx_result["attributeTypeName_size"] = attributeTypeName_size
    jdx_result["attributeTypeName_color"] = attributeTypeName_color


    final_jdx_result[code] = jdx_result


with open("./jdx_3-3_result.py", "w", encoding="utf-8") as f:
    json.dump(final_jdx_result, f, ensure_ascii=False)
