# Programming Languages Structures
# Exe 1.4
# Shir Kanner 214577213
# Shira Alkobi 326415353

def is_prime(n):
    if n == 0 or n == 1:
        return False

    result = list(filter(lambda y: n % y == 0, range(2, n)))
    return len(result) == 0

    # arr = [True] * (n + 1)
    # arr[0] = False

    # for i in range(2, int(n + 1 / 2)):
    #     if arr[i]:
    #         for m in range(i * 2, n + 1, i):
    #             if m == n:
    #                 return False
    #             else:
    #                 arr[m] = False
    #
    # return True


def find_prime_twin(n):
    # According to the instructions, we made an assumption that the parameter has to be prime.
    if is_prime(n + 2):
        return n + 2
    if is_prime(n - 2):
        return n - 2
    return None


def create_prime_dict(n):
    primes = list(filter(lambda x: is_prime(x), range(2, n)))
    return dict(map(lambda x: (x, find_prime_twin(x)), primes))

    # for i in range(2, n):
    #     if is_prime(i):
    #         dict[i] = find_prime_twin(i)
    #
    # return dict


num = input("enter prime number: \n")
if num.strip().isdigit():
    real_num = int(num)
    if is_prime(real_num):
        twin = find_prime_twin(real_num)
        if twin is None:
            print("invalid input")
        else:
            print(twin)
    else:
        print("invalid input")
else:
    print("invalid input")
