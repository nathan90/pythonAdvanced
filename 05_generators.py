# Generators allow us to look into one value at a time and to not store the entire sequence of numbers when we dont need to

class Generators:
    def __init__(self, n):
        self.n = n
        self.last = 0
    
    def __next__(self):
        return self.next()
    
    def next(self):
        if self.last == self.n:
            raise StopIteration()

        rv = self.last ** 2
        self.last += 1
        return rv

# g = Generators(100)

# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         break

# We are not storing the all the values in a list. All we are keeping track is the internal state of the next number we need to generate
# We don't need to store every single value. Only store the last value we generated and then using that we can generate the next

# The above statement is the equivalent of a generator


def gen(n):
    for i in range(n):
        yield i**2

# The yield keyword works as , as soon as we hit yield, it returns the value to wherever this was called, wherever we were looping through, and then it pauses the function rather than stopping the execution of this function. Which means we actually keep track of what value of i was

g = gen(100)

for i in g:
    print (i)


# Zclose generator ,stop generator , start generator