# scoping.level.2.py
def outer():
    test = 1  # outer scope

    def inner():
        test = 2  # inner scope
        print('inner:', test)

    inner()
    print('outer:', test)


test = 0  # global scope
outer()
print('global:', test)
