#Modify the behaviour of a function without changing any of the function code

# def func(string):
#     def wrapper():
#         print("started")
#         print(string)
#         print("ended")

#     return wrapper

# x = func("Hello")
# print(x)
# x()

# Functions in python are objects, which means we can pass them around our program

# def func(f):
#     def wrapper():
#         print("started")
#         f()
#         print("ended")

#     return wrapper

# def func2():
#     print("i am func2")

# def func3():
#     print("i am func3")

# # x = func(func2)
# x = func(func3)
# print(x)
# x()

# Instead of doing the above method, we can use the decorator method

# def func(f):
#     def wrapper(*args, **kwargs):#Accept any number of positional or keyword arguments
#         print("started")
#         f(*args, **kwargs)
#         print("ended")

#     return wrapper
# @func
# def func2(x):
#     print("i am func2", x)

# def func3():
#     print("i am func3")

# func3 = func(func3)
# func3()

# func2(1)

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func()
        total = time.time() - start
        print("Time: ", total)
        return rv

    return wrapper
    
@timer
def test():
    for _ in range(1000000):
        pass  

test()