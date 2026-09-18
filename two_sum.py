'''
在列表中找出两个不同位置的数字，使它们的和等于 target，返回它们的下标；如果找不到，返回 None
'''

def two_sum(numbers, target):
    """
    使用哈希表（字典）实现 O(n) 时间复杂度
    """
    seen = {}  # 存储 {数字: 索引}
    for i,num in enumerate(numbers):  #i和num的位置不能换，因为enumerate返回的就是(索引,值)的元组
        complement = target - num  # 需要的另一个数
        if complement in seen:
            return [seen[complement], i] #返回value
        seen[num] = i              #num为key，i为value，seen = {2:0,7:1...}
    return None
        
print(two_sum([2, 7, 11, 15], 9))