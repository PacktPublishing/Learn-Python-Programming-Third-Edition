# Local versus Global

# we define a function, called local
def local():
    m = 7
    print(m)

# we define m within the global scope
m = 5

# we call, or `execute` the function local
local()

print(m)
