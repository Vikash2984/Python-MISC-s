from functools import reduce
def big(first, second):
    flag = second > first
    if flag:
        g = second
    else:
        g = first
    return g
numbers = [100, 200, 300, 500, 400]
result = reduce(big, numbers)
print(result)
