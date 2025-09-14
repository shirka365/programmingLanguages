# Shir Kanner 214677213
# Shira Alkobi 326415353

from functools import reduce
import time
from itertools import accumulate

from Lib._pydatetime import timedelta, datetime

################################### QUESTION 1 ###################################

y = lambda x: x / 2 + 2

numbers = range(0, 10001)

newList = list(map(y, numbers))  # map numbers with lambda into a new list

startFunctional = time.time()  # measure the functional run time
totalFunctional = reduce(lambda a, b: a + b, newList)  # sum in a functional method
endFunctional = time.time()

print(f"Time for functional sum: {endFunctional - startFunctional} seconds")

startImperative = time.time()  # measure the imperative run time
totalImperative = 0
for value in newList:  # sum in a functional method
    totalImperative += value
endImperative = time.time()

print(f"Time for imperative sum: {endImperative - startImperative} seconds")

combinedSum = reduce(lambda a, b: a + b, list(map(y, numbers)))  # combine both operations to one code line

################################### END QUESTION 1 ###################################

################################### QUESTION 2 ###################################

numbers = list(range(1, 1001))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # create a list of the even numbers between 1-1000
odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))  # create a list of the odd numbers between 1-1000

#  create a lambda that maps each element in the list to the product of all elements up until the next element.
#  with a restriction of n elements
multiplyPrevious = lambda subEven, n: list(map(
    lambda x, next: x * next,  # takes each parameter from the lists, respectively
    list(accumulate(subEven[:n - 1], lambda x, y: x * y)),  # a list of the prefix products
    subEven[1:n]  # the original list, moved one place to the right
))

# create a lambda that operates a function on the current and next element
accAndAdd = lambda subOdd: list(map(
    lambda x, next: x / 2 + 2 + next,
    list(accumulate(subOdd)),
    subOdd[1:] + [0]))

# create a lambda that gets a function, the data to operate on , and optional arguments
# and apply the function n the data
apply_list_function = lambda func, data, *args: func(data, *args)

# apply the functions on respective lists
new_even = apply_list_function(multiplyPrevious, even_numbers, len(even_numbers))
new_odd = apply_list_function(accAndAdd, odd_numbers)

# sum and print
print(reduce(lambda x, y: x + y, new_even))
print(reduce(lambda x, y: x + y, new_odd))


################################### END QUESTION 2 ###################################


################################### QUESTION 3 ###################################

# a function that gets a date, number of dates to return , and number of days to jump
def get_dates(start_date_str, step_days, count):
    # parse the string of date to a datetime object
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()

    steps = range(0, step_days * count,
                  step_days)  # create a list where each elements is the number of days to jump from current date

    # map each element in the list to the date according to the jump and return the list of wanted dates
    return list(map(lambda d: (start_date + timedelta(days=d)).strftime("%Y-%m-%d"), steps))


dates = get_dates("2025-12-13", 7, 5)
print(dates)


################################### END QUESTION 3 ###################################

################################### QUESTION 4 ###################################

def power_function(n):  # a function that return a lambda that represent a power of n
    return lambda x: x ** n


power_of_2 = power_function(2)  # get x to the power of 2
power_of_3 = power_function(3)  # get x to the power of 3

result1 = power_of_2(2)
result2 = power_of_3(3)

print(result1, (power_function(2))(3))


# a function that returns a mapping object where for each number in 1-n range, gets a power function
def get_map(n):
    return map(lambda x: power_function(x), range(0, n))


n = int(input("Enter number of powers:"))
result = get_map(n)
base = int(input("Enter base:"))
print(type(result))
print(tuple(map(lambda x: x(base), result)))  # apply map result on the base


# get the approximation of e^x with a limit of n.
def get_taylor(x, n):
    taylor_nominators = list(map(lambda z: z(x), get_map(n)))  # list of nominators - x^n
    taylor_denominators = list(accumulate([1] + list(range(1, n + 1)), lambda x, y: x * y))  # list of denominators - n!
    taylor_list = list(
        map(lambda a, b: a / b, taylor_nominators, taylor_denominators))  # divide nominator by denominator
    return reduce(lambda a, b: a + b, taylor_list)  # sum to get approximation


################################### END QUESTION 4 ###################################

################################### QUESTION 5 ###################################

def task_manager():
    tasks = dict()  # create dictionary for the tasks

    def add_task(name, state="incomplete"):
        tasks[name] = state

    def get_tasks():
        return tasks

    def complete_task(task):
        tasks[task] = "complete"

    # return dictionary of possible operations to do on the task dictionary
    return {
        'add_task': add_task,
        'get_tasks': get_tasks,
        'complete_task': complete_task
    }


# Create a new task manager
tasks_manager = task_manager()
# Add tasks
tasks_manager['add_task']("Write email")
tasks_manager['add_task']("Shopping", "in progress")
tasks_manager['add_task']("Homework")
# Get the list of tasks
current_tasks = tasks_manager['get_tasks']()
print(current_tasks)
# Should print: {'Write email': 'incomplete', 'Shopping': 'in progress', 'Homework':'incomplete'}
# Mark a task as complete
tasks_manager['complete_task']("Write email")
# Get the list of tasks after marking and deleting
current_tasks = tasks_manager['get_tasks']()
print(current_tasks)
# Should print: {'Write email': 'complete', 'Shopping': 'in progress', 'Homework': 'incomplete'}

################################### END QUESTION 5 ###################################
