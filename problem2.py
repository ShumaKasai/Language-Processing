import re, collections

# 読み込み
with open(r"data\new_test.txt") as reader:
    content = reader.read()

# 並び替え
content = content.lower()
content = re.sub(r"[^a-z]","",content)
abc_count = collections.Counter(content)
print(abc_count)

# 書き出し
#with open(r"data\count_test.txt", 'w') as writer:
#    writer.write(abc_dict)