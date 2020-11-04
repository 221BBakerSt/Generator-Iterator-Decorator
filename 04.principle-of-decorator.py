def f1():
    print("--f1--")

def closure(func):
    def inner():
        print("--verification--")
        return func()
    return inner

# the closure function received a function name f1 as a parameter,
# the returned value inner was stored by innerFunc
innerFunc = closure(f1)

# so when innerFunc is called, it actually calls inner function
# inner function has a verification inside and returned the parameter function, f1, and called it f1()
# the returned function name was assigned back to f1
innerFunc()
# so in the end, the original f1 function was executed as usual but verification was invoked before it

print("-------------")
# now replace innerFunc with f1, so, inner was assigned to f1
f1 = closure(f1) 
# it looks like we called the original f1 function but actually verification was invoked before it
f1()

"""f1() looks unmodified, but it actually switched variable assignment, and most importantly, achieved verification process."""

print("-------------")
# the process above is equivalent to a decorator above the target function:
@closure
def f2():
    print("--f2--")

f2()

# result:
# --verification--
# --f1--
# -------------
# --verification--
# --f1--
# -------------
# --verification--
# --f2--
