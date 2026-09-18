'''
要求：
Employee 有姓名和基本工资
Manager 比基本工资多一个固定奖金
Developer 根据加班小时数和每小时加班费计算工资
三个类都实现同名方法：
使用同一个列表保存不同类型的员工，并循环输出每个人的工资
工资、奖金、加班小时数不能为负数
使用继承和方法重写
代码控制在 50 行以内
'''

class Employee:
    def __init__(self,name,basic_salary):  #初始化不要写return（默认返回None）
        if basic_salary < 0:
            raise ValueError("基本工资不能为负数")
        self.name = name
        self.basic_salary = basic_salary
        
    def totalsalary(self):
        return  self.basic_salary

    
class Manager(Employee):    #子类继承父类
    def __init__(self, name, basic_salary,reward):
        super().__init__(name, basic_salary)  #super()让子类复用父类的初始化逻辑，不只是初始化,见下
        if reward < 0:
            raise ValueError("奖金不能为负数")
        self.reward = reward
    
    def totalsalary(self):  #方法重写，子类同名函数覆盖父类
        return self.basic_salary + self.reward
    

class Developer(Employee):
    def __init__(self, name, basic_salary,per_hour,hour):
        super().__init__(name, basic_salary)
        if per_hour <= 0 or hour < 0:
            raise ValueError("加班时长或时薪不能为负数")
        self.per_hour = per_hour
        self.hour = hour
    
    def totalsalary(self):
        return self.basic_salary + self.per_hour * self.hour
    

employees = [
    Employee('小王', 5000),
    Manager('小李', 8000, 2000),
    Developer('小张', 6000, 10, 100)
]

for employee in employees:
    print(employee.name, employee.totalsalary())


'''
class Employee:
    def get_info(self):
        return f"姓名: {self.name}, 工资: {self.salary}"

class Manager(Employee):
    def get_info(self):
        basic_info = super().get_info()  # 先拿父类的信息
        return f"{basic_info}, 奖金: {self.bonus}"  # 再加上自己的

# 使用
m = Manager("小李", 8000, 2000)
print(m.get_info())  # 姓名: 小李, 工资: 8000, 奖金: 2000
'''