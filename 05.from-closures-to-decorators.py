""" To create a decorator: """

# First step: write a closure
def dec1():
    def v1():
        pass
    return v1

# Second step: the closure receives a function name as a parameter,
# and return the function in the end
def dec1(func):
    def v1():
        print("here is a verification function")
        # func is the target function
        return func()
    return v1

# Third step: define a target function
def target():
    print("this is a target function")
    return "target function"

# Fourth step: call the dec1 function
result = dec1(target)
# the target function is called after verification
print(result())

print("------------------------")

# Final step: replace dec1 function with a decorator above the target function
@dec1
def target():
    print("this is a target function")
    return "target function"

# the result is the same as the previous part
print(target())

print("----------multiple decorators:----------")

def dec1(func):
    print("---dec1---")
    def v1(*args, **kwargs):
        print("---verification---")
        result = "<div>" + func(*args, **kwargs) + "</div>"
        return result
    return v1

def dec2(func):
    print("---dec2---")
    def v2(*args, **kwargs):
        print("---log---")
        result = "<p>" + func(*args, **kwargs) + "</p>"
        return result
    return v2

# target function without parameters
@dec2
@dec1
def target():
    print(f"---without param---")
    return "without param"
a = target()
print(a)


# result:
# here is a verification function
# this is a target function
# target function
# ------------------------
# here is a verification function
# this is a target function
# target function
# ----------multiple decorators:----------
# ---dec1---
# ---dec2---
# ---log---
# ---verification---
# ---without param---
# <p><div>without param</div></p>
