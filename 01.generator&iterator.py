a = [x**2 for x in range(3)]
print(a)

# if it's a tuple, it becomes a generator
b = (x**2 for x in range(3))
print(b)

# a generator is an object stored in memory and the elements can't be directly printed out
print(next(b))
# each time next() is called, the next element is calculated
print(next(b))
print(next(b))
try:
    # if no element to iterate anymore, raise StopIteration
    print(next(b))
except StopIteration:
    print("b:", tuple(b))

# Since all elements in b have been iterated, we need to generate it again to apply for loop below to print each element.
b = (x**2 for x in range(3))
for x in b:
    print(x)

def enu(c):
    for _ in c:
        print(_)

c = enumerate(a, 0)
# enumerate object is also a generator
print(c)
enu(c)

print("-----------Iterable & Iterator-----------")
"""
Iterable means elements in an object can be printed by "for" loop
Iterator means elements in an object can be popped out by next() function
For an Iterator, it's uncertain how many elements can be called by next(). Every time next() is called, it pops out one element.
the elements in list/tuple/str/dict can be printed by for loop, so they are Iterable
the elements in list/tuple/str/dict are certain, so they are not Iterator
but an Iterable object can be turned into an Iterator with iter() function
"""
from collections.abc import Iterable, Iterator
# is a string iterable? is a string an iterator?
print(isinstance("", Iterable), isinstance("", Iterator))
# is a list iterable? is a list an iterator?
print(isinstance([], Iterable), isinstance([], Iterator))
# is a tuple iterable? is a tuple an iterator?
print(isinstance((), Iterable), isinstance((), Iterator))
# is a dict iterable? is a dict an iterator?
print(isinstance({}, Iterable), isinstance({}, Iterator))
# call iter() function to get an Iterator object
print(isinstance(iter([]), Iterable), isinstance(iter([]), Iterator))
n = iter("12")
print(next(n))
# n.__next__() equals to next(n)
print(n.__next__())

print('------------keyword yield------------')

def foo():
    print("step 1")
    yield 1
    print("step 2")
    yield 2
    print("step 3")
    yield 3
"""
keyword yield turns a function to a generator
Every time next() is called, the process pauses at yield, which works as keyword return.
The next time next() is called, the process continues from where it was paused.
"""
f = foo()
print(next(f))
print(next(f))
print(next(f))
# if no element to iterate anymore, raise StopIteration
# print(next(f))

print("-----------generate Fibonacci numbers----------")

def fibo(max):
    # regular method
    a = b = 1
    for _ in range(max):
        print(a, end=", ")
        a, b = b, a + b
    return "done"
print(fibo(6))

def fib(max):
    a = b = 1
    for _ in range(max):
        # use keyword yield, so it becomes a generator
        yield a
        a, b = b, a + b
    return "done"
# it's a generator
print(fib(100))

for x in fib(6):
    print(x, end=", ")

print("\nTo get the return value from the generator:")
generate = fib(6)
while True:
    try:
        x = next(generate)
        print("generate:", x)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break


# result:
# [0, 1, 4]
# <generator object <genexpr> at 0x10e954dd0>
# 0
# 1
# 4
# b: ()
# 0
# 1
# 4
# <enumerate object at 0x1036e9e60>
# (0, 0)
# (1, 1)
# (2, 4)
# -----------Iterable & Iterator-----------
# True False
# True False
# True False
# True False
# True True
# 1
# 2
# ------------keyword yield------------
# step 1
# 1
# step 2
# 2
# step 3
# 3
# -----------generate Fibonacci numbers----------
# 1, 1, 2, 3, 5, 8, done
# <generator object fib at 0x10db27e50>
# 1, 1, 2, 3, 5, 8, 
# To get the return value from the generator:
# generate: 1
# generate: 1
# generate: 2
# generate: 3
# generate: 5
# generate: 8
# Generator return value: done
