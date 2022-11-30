import re

# 読み込み
with open(r"data\test.txt") as reader:
    content = reader.read()

# 置換
content = content.lower()
content = re.sub(r"[^\s\na-z]"," ",content)

# 書き出し
with open(r"data\new_test.txt", 'w') as writer:
    writer.write(content)