# Programming Languages Structures
# Exe 1.2
# Shir Kanner 214577213
# Shira Alkobi 326415353

def sum_digit(n):
    try:
        real = int(n)
    except ValueError:
        return "invalid input"
    result = sum(map(lambda current_digit: int(current_digit), str(abs(real))))
    return result

    # result = 0
    # while real > 0:
    #     result += int(real) % 10
    #     real /= 10


num = input("enter number:\n")
print(sum_digit(num))
