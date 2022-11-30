import re, collections, random

# 読み込み
with open(r"data\test.txt") as reader:
    content = reader.read()

# 並び替え
content = content.lower()
content = re.sub(r"[^a-z]","",content)
abc_all = len(content)
abc_count = collections.Counter(content)
    
for i in range(100):
    n = random.choice(range(1,abc_all))
    print(content[n], end='')