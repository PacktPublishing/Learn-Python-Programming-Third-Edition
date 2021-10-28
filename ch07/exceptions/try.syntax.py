# exceptions/try.syntax.py

def try_syntax(numerator, denominator):
    try:
        print(f'In the try block: {numerator}/{denominator}')
        result = numerator / denominator
    except ZeroDivisionError as zde:
        print(zde)
    else:
        print('The result is:', result)
        return result
    finally:
        print('Exiting')

print(try_syntax(12, 4))
print(try_syntax(11, 0))


"""
$ python try.syntax.py
In the try block: 12/4    # try
The result is: 3.0        # else
Exiting                   # finally
3.0                       # return within else

In the try block: 11/0    # try
division by zero          # except
Exiting                   # finally
None                      # implicit return end of function
"""
