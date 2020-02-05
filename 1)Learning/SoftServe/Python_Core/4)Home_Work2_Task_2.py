Given_num = str(input('Enter whatever numbers you want to add:'))
# 1)FIRST PART
i = 0
list_of_numbers_given = list()
while i != len(Given_num):
    list_of_numbers_given.append(int(Given_num[i:i + 1]))
    i += 1
print(sum(list_of_numbers_given))
# 2)SECOND PART
print(Given_num[::-1])
# 3)THIRD PART
print(sorted(list_of_numbers_given))
