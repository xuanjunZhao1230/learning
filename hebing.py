'''
题目：合并两个有序列表
给定两个已经按升序排列的整数列表，请将它们合并成一个新的升序列表。
要求
不要直接使用:sort()  sorted()
使用两个索引分别遍历两个列表。
保留重复数字。
'''

'''
list1 = list(map(int, input("请输入第一个升序列表：").split()))
list2 = list(map(int, input("请输入第二个升序列表：").split()))

combine = list1 + list2
for m in range(len(combine)-1):
    for n in range(len(combine)-m-1):
        if combine[n] > combine[n + 1]:
            combine[n],combine[n + 1] = combine[n + 1],combine[n]
        
print(combine)
'''

#满分答案
list1 = list(map(int, input("请输入第一个升序列表：").split()))
list2 = list(map(int, input("请输入第二个升序列表：").split()))

result = []
i = 0
j = 0

while i < len(list1) and j < len(list2):
    if list1[i] <= list2[j]:
        result.append(list1[i])
        i += 1
    else:
        result.append(list2[j])
        j += 1

while i < len(list1):
    result.append(list1[i])
    i += 1

while j < len(list2):
    result.append(list2[j])
    j += 1

print(result)