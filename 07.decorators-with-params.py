"""a decorator with parameters is a closure wrapped by another function layer"""

def big(temp):
    def medium(func):
        def small(*args, **kwargs):
            print("Here is a log/verification")
            if "correct" == temp:
                print("Good job!")
                x = func(*args, **kwargs)
                return x
            else:
                print(temp)
                return "You are unauthorised"
        return small
    # add this extra layer to store the decorator parameter
    return medium

@big("correct")
def f1(a, b, c):
    print(f"Values are {a}, {b}, {c}")
    return "this is f1"

x = f1(11, 22, 33)
print(x)

@big("wrong")
def f2():
    print("---f2---")
    return "this is f2"

x = f2()
print(x)

# result:
# Here is a log/verification
# Good job!
# Values are 11, 22, 33
# this is f1
# Here is a log/verification
# wrong
# You are unauthorised
