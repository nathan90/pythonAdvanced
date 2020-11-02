# file = open("file.txt", "w")
# file.write("hello")
# file.close()

#Context manager. With is an example of context manager
# with open("file.txt", "w") as file:
#     file.write("hello WOlrd")

# class File:
#     def __init__(self, filename, method):
#         self.file = open(filename, method)

#     def __enter__(self):
#         print ("Enter")
#         return self.file

#     def __exit__(self, type, value, traceback):
#         print(f"{type}, {value}, {traceback}")
#         print ("Exit")
#         self.file.close()
#         if type == Exception:
#             return True # this will tell python the exception was handled and program willnot be crashed
    
# with File("file.txt", "w") as f:
#     print("Middle")
#     f.write("Helo!")
#     raise Exception()

# The exception will be raised afterwards. Regardless if there is an exception or not, we're gonna call the exit method, the point being we can handle an exception inside the exit method if we need to. The exception is passed to the EXIT FUNCITON


# context manager using generator
from contextlib import contextmanager

@contextmanager
def file(filename, method):
    print('Enter')
    file = open(filename, method)
    yield file
    file.close()
    print('Exit')

with file("text.txt", "w") as f:
    print("middle")
    f.write("Hello")