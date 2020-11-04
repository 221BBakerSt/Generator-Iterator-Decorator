def outside(num1):
    print("--1--")

    def inside(num2):
        print("--3--")
        print(num1, num2)

    print("--2--")
    return inside


x = outside(10)
# print the return value inside, it points to the reference of function inside
print(x)
print("--------------------")
x(20)
print("--------------------")

def coefficient(a, b):
    def parameter(x):
        y = a*x+b
        return y
    return parameter

value = coefficient(2, 1)
print(value(4))


# result:
# --1--
# --2--
# <function outside.<locals>.inside at 0x101188b90>
# --------------------
# --3--
# 10 20
# --------------------
# 9
