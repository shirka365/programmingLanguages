# Shir Kanner 214677213
# Shira Alkobi 326415353

from unpythonic import looped
import sys

sys.setrecursionlimit(2000)

# imports for handling with recursion maximum depth errors
from tail_recursive import tail_recursive
from tail_recurse import tail_call_optimized

# ==================EXE 1==================
def get_tuple(n=1000):
    """
    returns a tuple of the range 1-n
    n is set in default to be 1000, as requested in question
    """
    if n == 0:
        return ()
    # the recursion is backwards, insert to the end and then take care of the other in the beginning
    return get_tuple(n - 1) + (n,)


# print(get_tuple())

@tail_call_optimized
def tail_get_tuple(n, current_t=None):
    """
    returns a tuple of the range 1-n
    implemented in tail recursion
    """
    if current_t is None:   # initialization of tuple
        current_t = []
    if n == 0:
        return tuple(current_t)
    # insert the current n to the first place in the tuple
    # again, the recursion is backwards, from the end of th the tuple to its beginning
    current_t.insert(0, n)
    return tail_get_tuple(n - 1, current_t)  # adding the accumulative tuple in order to implement tail recursion


# result = tail_get_tuple(1000)
# print(result)



# ==================EXE 2==================
def total_sum(l):
    """
    returns the sum of array items
    """
    if len(l) == 1:
        return l[0]
    # return the sum of current item with the next items' sum
    return l[0] + total_sum(l[1:])


@tail_call_optimized
def tail_total_sum(l, sum=0):
    """
        returns the sum of array items
        implemented in tail recursion
    """
    if len(l) == 0:
        return sum
    # the accumulative sum is one of the recursion parameters, in order to support tail recursion
    return tail_total_sum(l[1:], sum + l[0])



# ==================EXE 3==================
def findLCM(n1, n2):
    # inner recursion function
    def rec_findLCM(big, small, i=1):
        """
        returns the first common multiple of the given parameters
        i is the current multiple counter of big that we check
        """
        # LCM is the first multiple of big that is also a multiple of small (i is set in default to 1)
        if (big * i) % small == 0:
            return big * i

        # the difference between a tail recursion and a regular recursion is the position of the rec function call
        # the only way we thought that can solve the problem was with tail recursion,
        # so we made the tiniest change in order to make it not a tail one -
        # the sum with 0 makes the rec function call not the last returned value
        return 0 + rec_findLCM(big, small, i + 1)

    # find the bigger value first and then send it to recursion
    if n1 > n2:
        return rec_findLCM(n1, n2)
    else:
        return rec_findLCM(n2, n1)


@tail_call_optimized
def tail_findLCM(n1, n2):
    # inner recursion function
    def rec_findLCM(big, small, i=1):
        """
        returns the first common multiple of the given parameters
        i is the current multiple counter of big that we check
        implemented in tail recursion
        """
        # LCM is the first multiple of big that is also a multiple of small (i is set in default to 1)
        if (big * i) % small == 0:
            return big * i
        # call recursion for the next multiple of big, according to next i
        return rec_findLCM(big, small, i + 1)

    # find the bigger value first and then send it to recursion
    if n1 > n2:
        return rec_findLCM(n1, n2)
    else:
        return rec_findLCM(n2, n1)



# ==================EXE 4==================
def isPalindrome(num):
    """
    returns whether a number is a palindrome
    """
    # convert the number to a string for an easy iteration
    digits = str(num)
    # divide it in the middle for checking the 2 halves
    h1 = digits[:int(len(digits) / 2)]
    h2 = digits[int(len(digits) / 2) + len(digits) % 2:]

    # inner recursion function
    def rec_isPalindrom(h1, h2, state=True):
        """
        returns whether a number is a palindrome (recursive)
        """
        # if we reached the end of one string, return true because all the characters were equal as needed
        if len(h1) == 0:
            return state
        # if the next characters from the two halves aren't equal, the state is false,
        # we return the value and not continue
        if h1[0] != h2[-1]:
            state = False
            return state
        # the recursive call is continuing only if the state and the next recursive call are true
        return state and rec_isPalindrom(h1[1:], h2[:-1], state)

    return rec_isPalindrom(h1, h2)


@tail_call_optimized
def tail_isPalindrome(num):
    """
    returns whether a number is a palindrome
    implemented in tail recursion
    """
    # convert the number to a string for an easy iteration
    digits = str(num)
    # divide it in the middle for checking the 2 halves
    h1 = digits[:int(len(digits) / 2)]
    h2 = digits[int(len(digits) / 2) + len(digits) % 2:]

    def rec_isPalindrom(h1, h2):
        """
        returns whether a number is a palindrome (recursive)
        """
        # if we reached the end of one string, return true because all the characters were equal as needed
        if len(h1) == 0:
            return True
        # if the next characters from the two halves aren't equal, this isn't a palindrome
        if h1[0] != h2[-1]:
            return False
        # return if the next characters of the two strings can be a palindrome
        return rec_isPalindrom(h1[1:], h2[:-1])

    return rec_isPalindrom(h1, h2)



# ==================EXE 5==================
def sort_and_zip(l):
    """
    returns the sorted zip of the given list (l) items
    the items are lists, which we will need to sort before zipping
    """
    # inner recursion function
    def rec_sort(rec_l):
        """
        sorts each of the lists stored in the given list
        """
        # if we reached the last list, sort it and return
        if len(rec_l) == 1:
            return [sorted(rec_l[0])]
        # return the first sorted list with the sorted next lists
        return [sorted(rec_l[0])] + rec_sort(rec_l[1:])

    result = rec_sort(l)
    # after sorting the list items, zip them
    return zip(*result)


# print(list(sort_and_zip([[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']])))


@tail_call_optimized
def tail_sort_and_zip(l):
    """
   returns the sorted zip of the given list (l) items
   the items are lists, which we will need to sort before zipping
   implemented in tail recursion
   """

    # inner recursion function
    def rec_sort(rec_l, acc=None):
        """
        sorts each of the lists stored in the given list
        """
        # initializing the accumulative list which includes the sorted lists
        if acc is None:
            acc = []
        # when reaching the end of the list, return the accumulative list with the sorted items
        if not rec_l:
            return acc

        # add to the accumulative list the new sorted item
        acc.append(sorted(rec_l[0]))
        # call the sorting for the next list items, with the accumulative list
        return rec_sort(rec_l[1:], acc)

    result = rec_sort(l)
    # after sorting the list items, zip them
    return zip(*result)


# print(list(tail_sort_and_zip([[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']])))
