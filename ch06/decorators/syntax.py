# decorators/syntax.py
# This is not a valid Python module - Don't run it.

# ONE DECORATOR
# def func(arg1, arg2, ...):
#     pass

# func = decorator(func)

# # is equivalent to the following:

# @decorator
# def func(arg1, arg2, ...):
#     pass


# # TWO DECORATORS
# def func(arg1, arg2, ...):
#     pass

# func = deco1(deco2(func))

# # is equivalent to the following:

# @deco1
# @deco2
# def func(arg1, arg2, ...):
#     pass

# # DECORATOR WITH ARGUMENTS
# def func(arg1, arg2, ...):
#     pass

# func = decoarg(arg_a, arg_b)(func)

# # is equivalent to the following:

# @decoarg(arg_a, arg_b)
# def func(arg1, arg2, ...):
#     pass
