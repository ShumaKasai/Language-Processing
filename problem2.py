import re
import collections

# 読み込み
with open(r"data\new_test.txt") as reader:
    content = reader.read()

# 置換
content = content.lower()
content = re.sub(r"[^a-z]","",content)
c = collections.Counter(content)

# 書き出し
#with open(r"data\count_test.txt", 'w') as writer:
#    writer.write(abc_dict)
print(c.most_common())