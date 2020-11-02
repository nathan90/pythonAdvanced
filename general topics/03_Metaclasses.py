# Meta classes explained
# use only when needed. very complex so use only if absolutely necessary
 
 # In python, classes are actually objects
#  Objects can be passed around through parameters, store it, save it, interact during runtime
 # Class defines the rules for an object, defines attributes, parameters, methods that can be performed 
 # meta class defines the rules for a class

# class Test:
#     pass

# print(Test)
# print(Test())

# print(type(Test)) # returns meta class <class 'type'>
# class type is essentially what defines the rules and creates the class for us
# when we use class syntax we will call a type constructor using the different things in our class to make this class object

# class Foo:
#     def show(self):
#         print('Hi')

# def add_attribute(self):
#     self.z = 9
# Actual syntax for class declaration
# Test = type('Test', (Foo,), {"x": 5, "add_attribute": add_attribute})
# print(Test)
# print(Test())
# t = Test()
# t.wy = "Hello"
# print(t.wy)
# t.show()
# t.add_attribute()
# print(t.z)

# Meta class is above the classes we are creating with using class definition

class Meta(type):
    def __new__(self, class_name, bases, attrs):# New method is called before the init method
        print(attrs)
        a = {}
        # below we modify the metaclass and takes in attributes and function and convert to uppercase
        # 
        for name, val in attrs.items():
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] = val
        print(a)
        return type(class_name, bases, a)

class Dog(metaclass= Meta):
    x = 8
    y = 5
    
    def hello(self):
        print("Hi")

d = Dog()
# print(d.X)
# The default meta class of Dog is type. That is how all classes are created. We have in the code above overwritten that and changed it to our own meta class. We added own piece to the New dunder method that prints out the attribute and returns to us the object of class Dog