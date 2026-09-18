'''
给定一个字符串，请统计每个单词出现的次数。
要求：
忽略大小写（Python 和 python 认为相同）。
去掉单词前后的标点符号（只考虑 .,!? 四种）。
输出按照出现次数降序排列。
如果次数相同，则按字母序升序排列。
'''


text = input('please input text = ')
words = text.lower().split()
print(words)
counts = {}
for word in words:
    word = word.strip('.,!?')
    if word:
        counts[word] = counts.get(word,0) + 1

print(counts.items())

result = sorted(
    counts.items(),
    key=lambda item: (-item[1], item[0])
)

print(result)

for word, count in result:
    print(word, count)

