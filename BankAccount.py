'''
面向对象的题，不使用列表统计或字典算法。
要求：
账户有 owner 和 balance 属性
deposit(amount)：存款，金额必须大于 0
withdraw(amount)：取款，金额不能超过余额
存款或取款成功返回 True, 失败返回 False
余额不能变成负数
代码控制在 50 行以内
'''

class BankAccount:
    def __init__(self,name,account):
        self.name = name
        self.account = account

    def deposit(self,num):
        if num <= 0:
            return False
        self.account = self.account + num
        print(f"存入{num}")
        return True
    
    def withdraw(self,n):
        if n > self.account or n <= 0:
            return False
        self.account = self.account - n
        print(f"取出{n}")
        return True
    
    def money(self):
        if self.account < 0:
            return False
        return self.account
        
zhanghu = BankAccount('张三', 1000)
zhanghu.deposit(800)
zhanghu.withdraw(200)
print(f"当前账户余额为{zhanghu.money()}")   #如果用print(f"{zhanghu.account}")得到账户余额的话money()没被调用,可以删掉
