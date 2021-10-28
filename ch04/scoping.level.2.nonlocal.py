# scoping.level.2.nonlocal.py
def outer():
    test = 1  # outer scope

    def inner():
        nonlocal test
        test = 2  # nearest enclosing scope (which is 'outer')
        print('inner:', test)

    inner()
    print('outer:', test)


test = 0  # global scope
outer()
print('global:', test)
