
def add(x, y):
    """add Function"""
    return x + y

def subtract(x, y):
    """subtract function"""
    return x - y

def multiply(x, y):
    """multiply function"""
    return x * y

def divide(x, y):
    """division function"""
    if y == 0:
        raise ValueError('Cannot divide by zero')
    return x / y