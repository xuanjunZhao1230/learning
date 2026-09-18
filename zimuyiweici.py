'''
如果两个字符串包含的字母种类和数量都相同，只是顺序不同，则返回 True，否则返回 False。
要求：
不区分大小写
忽略空格
时间复杂度尽量为 O(n)
不使用现成的排序方法直接比较
'''

def is_anagram(s1,s2):
    s1 = s1.replace(' ','').lower()     #repalce(old,new)把old替换成new    .lower()大写全部转化为小写
    s2 = s2.replace(' ','').lower()
    counts1 = {}
    counts2 = {}
    for char in s1:
        counts1[char] = counts1.get(char,0) + 1
    for char in s2:
        counts2[char] = counts2.get(char,0) + 1
    print(counts1 == counts2)


is_anagram('sD fg','gfsd')

