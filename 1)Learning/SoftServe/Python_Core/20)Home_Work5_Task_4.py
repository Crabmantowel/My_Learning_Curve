def create_array(n):
    res = []
    i = 1
    while i != n + 1:
        res += [i]
        i += 1
    return res


some_array = int(input('Enter number for array: '))
print(create_array(some_array))
