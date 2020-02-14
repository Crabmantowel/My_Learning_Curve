# TASK ONE
# quantity = [int(input()) for i in range(int(input('How long is your list?: ')))]
# print(min(quantity), max(quantity))

#TASK TWO
# some_great_list = list(range(10))
# print([some_number_in_range for some_number_in_range in some_great_list if some_number_in_range % 2 == 0])
# print([some_number_in_range for some_number_in_range in some_great_list if some_number_in_range % 3 == 0])
# print([some_number_in_range for some_number_in_range in some_great_list if some_number_in_range % 2 != 0 and some_number_in_range % 3 != 0])

#TASK THREE
# factorial_up_to = (int(input('Enter number to which you wish get factorial: ')))
# base_number = 1
# factorial_made = [base_number * i for i in range(1, factorial_up_to + 1)]
# print(factorial_made)

#TASK FOUR
# Answer = input('Answer: ')
# while Answer != 'First':
#     print('Wrong answer')
#     Answer = input('Answer: ')
# print('Correct')

#TASK FIVE
# Answer = int(input('Answer: '))
# while Answer > 0 and Answer != 0:
#     Answer = int(input('Answer: '))
# print('Goodbye')

#TASK SIX
# taken_list = ([int(input()) for some_int in range(int(input('List length: ')))]) How can i implement if statement for negatives and Zero?
# print(list(range(1, int(input('List length: ')) + 1))=int(input('Enter {} position in your list: '.format numero)) if numero > 0 and numero != 0 else break))  # too much for one line, and not working though

List_range = list(range(int(input('How long is your list?: '))))
for position in List_range:
    replacer_num = int(input('Enter number: '))
    if replacer_num < 0 or replacer_num == 0:
        print('You`ve entered Zero or Negative Number, Quitting now')
        break
    else:
        List_range[position] = replacer_num
print(List_range)
