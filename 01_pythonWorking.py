#python is an interpreted language
# compiler takes higher level code and translates it into low level code byte code
# interpreter takes bytecode, read that on the fly and runs the code
# this is the reason why there is lot of issues with python running on machines like mobile devices etc that
# dont have a python interpreter because the byte code cannot be directly understood by the cpu. It need some 
# kind of interpreter to run it

# when we use something like c, depending on the compiler, we will compile our code directly to machine code 
# which means that it can be directly ran on the operating system without the need of an interpreter

#example 1
# class Dog:
#     def __init__(self):
#         self.bark()

# A lot of the code is actually executed at run time, not at compile time. 
# All that the compiler does is to translate it into bytecode and not necessarily
# check if all the code is valid
# So this means you can make the errors like this in the code and the compiler 
# doesnt pick it up and will be caught
# only during run time

# def make_class(x):
#     class Dog:
#         def __init__(self, name):
#             self.name = name

#         def print_value(self):
#             print(x)

#     return Dog

# cles = make_class(10)
# print(cles)

# make_class function took an argument x, we had a class dog defined inside the function. The reason we can do this is the python compiler doesnot check if this is valid or not. As long as you have valid syntax, correct format, your python code can run and execute fine. 
# Python reads from top to bottom, left to the right

# We created a class that uses a value from the function argument and we returned the class itself, not an instance of the class. Since python is executed on the fly, all the things we define in the code are being stored in the memory. So the dog class actually has a memory location for it 

# Now make an instance of the class
# print(type(cles))# cles is of type class
# d = cles('Tim')# create instance of the class
# print (d.name)
# d.print_value()

# Define a function inside a for Loop
# for i in range(10):
#     def show():
#         print(i*2)
#     show()

def func(x):
    if x == 1:
        def rv():
            print("X is equal to 1")
    else:
        def rv():
            print("X is not 1")

    return rv
import inspect
from queue import Queue
new_func = func(2)
new_func()
print(id(new_func)) # id gives the memory address of the function
# The inspect module 
# print(inspect.getmembers(new_func)) # gives the details of the function

# print(inspect.getsource(new_func))# gives the source code of the function

print(inspect.getsource(Queue)) # shows all the code used by python to create the queue class
