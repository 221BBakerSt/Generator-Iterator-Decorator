# this is also a general decorator function no matter with or without params
def outter(func):
    print("---start outter---")
    
    def inner(*args, **kwargs):
        print("---start inner---")
        print("hello inner")
        print("---end inner---")
        return func(*args, **kwargs)

    print("---end outter---")
    return inner

@outter
def func1():
    return "No values"

@outter
def func2(a, b):
    return f"The values are {a} and {b}"

@outter
def func3(a, b, c=33, d="ok"):
    # c and d are positional and keyword parameters
    return f"The values are {a}, {b}, {c} and {d}"


print(func1())
print(func2(2,3))
print(func3(11,22,d=44))


# result:
# ---start outter---
# ---end outter---
# ---start outter---
# ---end outter---
# ---start outter---
# ---end outter---
# ---start inner---
# hello inner
# ---end inner---
# No values
# ---start inner---
# hello inner
# ---end inner---
# The values are 2 and 3
# ---start inner---
# hello inner
# ---end inner---
# The values are 11, 22, 33 and 44
