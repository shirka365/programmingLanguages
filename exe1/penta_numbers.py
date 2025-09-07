# Programming Languages Structures
# Exe 1.1
# Shir Kanner 214577213
# Shira Alkobi 326415353

def get_penta_num(n):
    return int((n * (3 * n - 1)) / 2)


def pentaNumRange(n1, n2):
    return list(map(lambda x: get_penta_num(x), range(n1, n2)))