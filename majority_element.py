'''
给定一个非空整数列表，其中一定有一个数字出现次数超过列表长度的一半，请找出这个数字。
要求：
使用字典统计次数
不使用 sort() 排序
时间复杂度为 O(n)
代码控制在 50 行以内
'''

def majority_element(numbers):
    a = {}
    for num in numbers:
        a[num] = a.get(num,0) + 1

    print(a)

    for num,i in a.items():
        if i > len(numbers)//2:
            return num
    return None


print(majority_element([1,2,3,1,3,2]))