'''
# TASK ONE
a = int(input('Print your number'))
b = int(input('Print your number'))

if a > b:
    print('{} is bigger', a)
elif a < b:
    print('%s is bigger', b)
else:
    print('They are equal')

# TASK TWO
a = int(input('Type in a number: '))
print('number is even' if int(a % 2) else 'number is odd')

#TASK TREE


def my_facto(num):
    factorial = 1
    for numbers in list(range(1, num + 1)):
        factorial *= numbers
    return factorial


someones_number = int(input('Type in your factorial number'))
print(my_facto(someones_number))

#TASK FOUR
zero = 100
while zero != 0:
    zero -= 2
    print(zero)

for num in list(range(0, 100, 2)):
    print(num)

#TASK FIVE
#Var 1
for num in list(range(1, 100)):
    if num % 2:
        print(num)
    else:
        continue
#Var 2
print(list(range(1, 100, 2)))

#TASK SIX
some_unknown_list = [1, 25, 101, 3564, 782]
for some_number in some_unknown_list:
    if some_number % 2:
        pass
    else:
        print('there is an odd number, it`s ', some_number)
        break

#TASK SEVEN
numbers_in_a_list = [2, 3, 6, 4, 5]
counter = 0
for some_iterator in numbers_in_a_list:
    numbers_in_a_list[counter] = float(numbers_in_a_list[counter])
    counter += 1
print(numbers_in_a_list)
'''
#TASK EIGHT
n_num, first_num, second_num = int(input('Enter number for fibonacci sequence: ')), 0, 1
while first_num < n_num:
    print(first_num)
    first_num, second_num = second_num, first_num + second_num
