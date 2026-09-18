'''
使用 items 保存商品信息
add_item(name, price, quantity)：添加商品
remove_item(name)：删除商品
total_price()：计算购物车总价
商品价格和数量必须大于 0
删除不存在的商品时返回 False
代码控制在 50 行以内
'''

class ShoppingCart:
    def __init__(self):
        self.items = {}
        
    def add_item(self,name,num,per_price):
        if num <= 0 or per_price <= 0:
            return False
        elif name in self.items.keys():
            self.items[name]["数量"] += num
        else:
            self.items[name] = {"数量": num, "单价": per_price}
        return True

    def remove_item(self,name,n):
        if name not in self.items:
            return False
        current_num = self.items[name]["数量"]
        if n >= current_num:
            del self.items[name]
        else:
            self.items[name]["数量"] = current_num - n
        return True
    
    @property
    def total_price(self):
        total = 0
        for i in self.items.values():
            total = total + i["数量"] * i["单价"]
        #print(self.items)
        return total
    

cart = ShoppingCart()

cart.add_item('苹果', 5, 2)
cart.add_item('牛奶', 8, 1)
cart.add_item('奶茶',1,15)
cart.add_item('苹果', 5, 2)
print(cart.total_price)