# return.multiple.py
def moddiv(a, b):
    return a // b, a % b


def test(n=10**4):
    from random import choice, random, randint
    m = 10 ** 6
    for x in range(n):
        a = choice((randint(0, m), m * random()))
        b = 0
        while not b:
            b = choice((randint(1, m), m * random()))

        r = divmod(a, b)
        r2 = moddiv(a, b)
        if r != r2:
            print('Difference: ', a, b, r, r2)


if __name__ == "__main__":

    test(10 ** 6)
    print('Done')

    print(moddiv(20, 7))  # prints (2, 6)
