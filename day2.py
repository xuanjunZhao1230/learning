
#输出斐波那契数列的第n个数
def fib(n):
    if n < 1:
        return False
    elif n == 1:
        return 1
    
    result = []
    a = 0
    b = 1
    while len(result) < n:
        result.append(b)
        a , b = b , a+b

    return result[n-1]




#判断是否为质数
def is_prime(n):
    if n < 2:
        return False
    for num in range(2,n):
        if n % num == 0:
            return False
    return True
#求100以内的质数（不调用函数也可以）
'''
prime = []
for m in range(1,101):
    if is_prime(m):
        prime.append(m)

print(prime)
'''


#判断是否为水仙花数
def shuixian(n):
    for i in range(100,1000):
        c = i % 10
        b = (i // 10) % 10
        a = i // 100
        if i == 100 * a + 10 * b + c:
            return True
    return False


#(1,n+1)阶乘求和
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def factorial_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + factorial(i)
    return sum

#print(factorial_sum(3))        

#判断是否为回文数
'''
def huiwen(n):
    l = list(map(int, str(n))) 
    reversed_l = l[::-1] 
    #num = int(''.join([str(d) for d in reversed_l]))
    if l == reversed_l:
        return True
    return False
'''
def huiwen(n):
    s = str(n)
    #print(s[::-1])
    return s == s[::-1]










'''
a = 321
b = 123
print('%d * %d = %d' % (a, b, a * b))
print(f'{a} * {b} = {a*b}')
print('a*b=' f'{a*b}')
print("%.4f" %a)
'''