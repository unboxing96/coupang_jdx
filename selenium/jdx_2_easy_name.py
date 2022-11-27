# ori_name = {"name": "6층_JDX_ 여성 조직감 배색 요꼬에리_X2TST6565BE_평촌점"}

# sellerProductName: 등록상품명 (발주서에 사용되는 상품명)
# displayProductName: 노출상품명 (실제 쿠팡 판매페이지에서 노출되는 상품명.[brand]+[generalProductName]과 동일하게 입력할 것을 권장, 미입력 상태로도 등록 가능)
# generalProductName: 제품명 (구매옵션[Attribute exposed] 정보(사이즈, 색상 등)를 포함하지 않는 상품명)


### new name = {gender} + {season} + {brand_line} + {final_style} + {cate_gory} + {color}


import json
import pickle
import re

# get jdx_1-2_info.py
with open(
    "/Users/taehyeon/Desktop/jdxcode_0409/selenium/jdx_1-5_info.py",
    "r",
    encoding="utf-8",
) as f:
    codes = json.load(f)


# 복종 코드에 대응하는 키워드
with open(
    "/Users/taehyeon/Desktop/jdxcode_0409/selenium/jdx_1-2_category_keyword_color.py",
    "r",
    encoding="utf-8",
) as ff:
    category_keyword_color = json.load(ff)

# 노출 상품명 키워드
with open(
    "/Users/taehyeon/Desktop/jdxcode_0409/selenium/jdx_1-4_keyword_list.py",
    "r",
    encoding="utf-8",
) as ffff:
    k_list = json.load(ffff)
    keyword_list = k_list["keyword_list"]


for code in codes:
    new_name = {}

    # 성별 gender
    if code[5] in ["1", "2", "3", "4", "9"]:
        gender = "남성"
    elif code[5] in ["5", "6", "7", "8", "0"]:
        gender = "여성"
    else:
        gender = "공용"

    # 계절 season
    if code[5] in ["1", "5"]:
        season = "봄"
    elif code[5] in ["2", "6"]:
        season = "여름"
    elif code[5] in ["3", "7"]:
        season = "가을"
    elif code[5] in ["4", "8"]:
        season = "겨울"
    else:
        season = "사계절"

    # 브랜드_라인 brand_line
    if code[:2] == "X1":
        brand_line = "골프"
    else:
        brand_line = ""

    # 복종 category
    if code[2:4] in category_keyword_color["keyword"].keys():
        cg_keyword = category_keyword_color["keyword"]
        cate_gory = cg_keyword[code[2:4]]

    # 색상 color
    if code[9:11] in category_keyword_color["color"].keys():
        cg_color = category_keyword_color["color"]
        color = cg_color[code[9:11]]
    else:
        color = ""

    # new_name 변수 jdx_1-2_info.py에 추가
    new_name_2 = f"{gender} {season} {brand_line} {cate_gory} {color}"  # str
    new_name_1 = re.sub(" +", " ", new_name_2)
    new_name = {"new_name": new_name_1}
    codes[code].append(new_name)

# print(codes)


with open(
    "/Users/taehyeon/Desktop/jdxcode_0409/selenium/jdx_2-1_result_easy_name.py",
    "w",
    encoding="utf-8",
) as fff:
    json.dump(codes, fff, ensure_ascii=False)
