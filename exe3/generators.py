# Shir Kanner 214677213
# Shira Alkobi 326415353
import time
import math
from functools import reduce

# ==================EXE 1.1==================
def get_range(n=10000):
    """
    returns a list of the numbers from range 0-n.
    n is set in default to be 10000, as requested in question
    """
    return list(range(n+1))

# checking execution time of non-lazy function, and size of the returned object, for later comparison
start = time.time()
result1 = list(get_range())
end = time.time()

print("Result: ", result1)
print("Execution time: ", (end - start))
print("Object size: ", result1.__sizeof__())


def lazy_get_range(n=10000):
    """
    implemented lazy evaluation, using a generator
    returns a list of the numbers from range 0-n.
    n is set in default to be 10000, as requested in question
    """
    return (i for i in range(n + 1))

# checking execution time of lazy function, and size of the returned object
start = time.time()
result2 = list(lazy_get_range())
end = time.time()

print("Result: ", result2)
print("Execution time: ", (end - start))
print("Object size: ", result2.__sizeof__())



# ==================EXE 1.2==================
def get_first_5000(l):
    """
    out of the given list, return the 5000 first items
    """
    return l[:5001]

# checking execution time of non-lazy function, and size of the returned object
start = time.time()
result3 = list(get_first_5000(result1))
end = time.time()

print("Result: ", result3)
print("Execution time: ", (end - start))
print("Object size: ", result3.__sizeof__())


def lazy_get_first_5000(l):
    """
    implemented lazy evaluation, using a generator
    out of the given list, return the 5000 first items
    """
    return (l[i] for i in range(5001))

# checking execution time of lazy function, and size of the returned object
start = time.time()
result4 = list(lazy_get_first_5000(result1))
end = time.time()

print("Result: ", result4)
print("Execution time: ", (end - start))
print("Object size: ", result4.__sizeof__())

# comparing whether the two returned types are the same
print("Lazy and non-lazy return the same object type?: ", type(result3) == type(result4))



# ==================EXE 2==================
# help function for checking prime numbers, we already defined it in exe 1
def is_prime(n):
    if n == 0 or n == 1:
        return False

    result = list(filter(lambda y: n % y == 0, range(2, n)))
    return len(result) == 0


def return_prime():
    """
    generator for prime numbers
    """
    i = 1
    while True:
        if is_prime(i):
            yield i
        i += 1



# ==================EXE 3==================
def get_taylor(x, n):
    """
    returns the approximation of e^x with a limit of n.
    for each iteration (1-n), it prints the Taylor series next sum
    uses generator in order to receive each of the Taylor series items
    """
    # initializing the generator
    taylor_g = taylor_gen(x)
    # returning the total sum of the series items, in order to get the right approximation
    return reduce(lambda y, z: y+z, list(map(lambda a: next(taylor_g), range(n))))


def taylor_gen(x):
    """
    generator for returning the Taylor series items, given x
    """
    # initializes n (approximation limit)
    # and the inner sum of items (used for printing, does not affect the return value)
    inner_sum = 0
    n = -1
    while True:
        n += 1
        # calculates the next item in series - x^n / n!
        result = x ** n / math.factorial(n)
        # printing the current series sum
        inner_sum += result
        print(inner_sum)
        yield result


# print(get_taylor(2, 8))
