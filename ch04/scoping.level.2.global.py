# scoping.level.2.global.py
def outer():
    test = 1  # outer scope

    def inner():
        global test
        test = 2  # global scope
        print('inner:', test)

    inner()
    print('outer:', test)


test = 0  # global scope
outer()
print('global:', test)
