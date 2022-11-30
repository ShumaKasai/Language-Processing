import re

# 読み込み
with open(r"data\new_test.txt") as reader:
    content = reader.read()

# 置換
content = content.lower()
content = re.sub(r"[^a-z]","",content)
abc_dict = {i: content.count(i) for i in content}
#print(abc_dict)
# 書き出し
#with open(r"data\count_test.txt", 'w') as writer:
#    writer.write(abc_dict)
abc_dict = sorted(abc_dict.items())
print(abc_dict)