# Programming Languages Structures
# Exe 1.6
# Shir Kanner 214577213
# Shira Alkobi 326415353

def double(x):
    return 2 * x


def square(x):
    return x * x


def opposite(x):
    return (-1) * x


def activate_funcs(numbers, funcs):
    return dict(map(lambda func: (func.__name__, list(map(func, numbers))), funcs))


f = list([double, square, opposite])
print(activate_funcs([1], f))
