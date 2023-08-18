import json

# 读取 JSON 文件
with open('agronet_questions.json', 'r') as json_file:
    data = json.load(json_file)

# 计算记录数
record_count = len(data)

print(f"JSON 文件中有 {record_count} 条记录。")
