def decorator(function):
    def wrapper():
        print("hello")
        function()
        print("finish")
    return wrapper

@decorator
def nihao(a):
    print("nihao")
