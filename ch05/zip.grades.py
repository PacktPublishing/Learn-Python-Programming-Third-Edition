# zip.grades.py
# This is not a valid Python module - Don't run it.


grades = [18, 23, 30, 27]
avgs = [22, 21, 29, 24]

list(zip(avgs, grades))

list(map(lambda *a: a, avgs, grades))  # equivalent to zip
