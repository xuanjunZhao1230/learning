"""
面试题：找出字符串中第一个只出现一次的字符

要求：编写 first_unique_char(text) 函数，返回 text 中第一个只出现一次的
字符；如果不存在，返回 None。

示例：
first_unique_char('swiss') 返回 'w'
first_unique_char('aabb') 返回 None

要求时间复杂度为 O(n)，不要对每个字符反复调用 count 方法。
"""

def first_unique_char(text):
    counts = {}
    for char in text:             # 写入value后python会自动写入key！！！counts[char] = 1 会把 char 作为键、1 作为值保存
        if char in counts:        # 如果字符已经在字典中
            counts[char] += 1     # 值加 1
        else:                     # 如果字符第一次出现
            counts[char] = 1      # 初始化为 1
    
    for char in text:
        if counts[char] == 1:
            return char
    return None

if __name__ == '__main__':
    print(first_unique_char('zhaoxuanjun'))
    

