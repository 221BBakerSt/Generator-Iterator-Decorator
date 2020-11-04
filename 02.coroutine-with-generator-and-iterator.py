# There are 3 methods of multi-tasking: process, thread, coroutine.

from time import sleep

def f1():
    while 1:
        print("---1---")
        yield None
        sleep(0.5)

def f2():
    while 1:
        print("---2---")
        # nothing after yield is equivalent to yield None
        yield
        sleep(0.5)

a = f1()
b = f2()
for _ in range(3):
    next(a)
    b.__next__()

def f3(n):
    for _ in range(3):
        print("---3---")
        next(n)
        sleep(0.5)

a = f1()
f3(a)

# result:
# ---1---
# ---2---
# ---1---
# ---2---
# ---1---
# ---2---
# ---3---
# ---1---
# ---3---
# ---1---
# ---3---
# ---1---
