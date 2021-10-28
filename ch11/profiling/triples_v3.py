
def calc_triples(mx):
    triples = []
    for a in range(1, mx + 1):
        for b in range(a, mx + 1):
            hypotenuse = calc_hypotenuse(a, b)
            if is_int(hypotenuse):
                triples.append((a, b, int(hypotenuse)))
    return triples


def calc_hypotenuse(a, b):
    return (a*a + b*b) ** .5


def is_int(n):
    return n == int(n)


triples = calc_triples(1000)

"""
$ python -m cProfile profiling/triples_v3.py
         1002038 function calls in 0.269 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   500500    0.084    0.000    0.084    0.000 triples_v3.py:13(calc_hypotenuse)
   500500    0.068    0.000    0.068    0.000 triples_v3.py:17(is_int)
        1    0.000    0.000    0.269    0.269 triples_v3.py:3(<module>)
        1    0.116    0.116    0.269    0.269 triples_v3.py:3(calc_triples)
        1    0.000    0.000    0.269    0.269 {built-in method builtins.exec}
     1034    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
