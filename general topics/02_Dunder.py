# import inspect

# x = [1, 2, 3]
# y = [4, 5]

# print(x+y)
# # class list is implemented under the hood

class Person:
    def __init__(self, name):
        self.name = name
    # repr allows us to define the string representation of an object
    def __repr__(self):
        return f"Person({self.name})"

    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Invalid argument, must be an int")
        self.name = self.name * x

    def __call__(self, y):
        print("called this function ", y)

    def __len__(self):
        return len(self.name)

# all the above are data model methods or dunder methods

# p = Person("tim")
# # p * 4
# p(4)
# print(len(p))


from queue import Queue as q
import inspect
# q = Queue()
# print(q)
# print(inspect.getsource(Queue))

class Queue(q): #Our own class Queue which extends from q (original Queue)
    def __repr__(self):
        return f"Queue({self._qsize()})"
    # add an item to the queue 
    def __add__(self, item):
        self.put(item)
qu = Queue()
qu+7
qu+9
print(qu)

# Each of the unique syntax that we use in the higher level like addition of lists translates down to 
# lower level dunder methods that implement that operation

