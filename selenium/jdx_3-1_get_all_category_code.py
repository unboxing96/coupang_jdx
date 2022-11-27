import json

with open(
    "/Users/taehyeon/Desktop/jdxcode_0409/selenium/jdx_3-3_result.py",
    "r",
    encoding="utf-8",
) as f:
    all_data = json.load(f)

all_category = []
for data in all_data:
    all_category.append(all_data[data]["displayCategoryCode"])

sort_of_category = list(set(all_category))
print(sort_of_category)
print(len(sort_of_category))
