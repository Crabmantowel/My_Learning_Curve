import sys

# TASK ONE
# def mid_arithmetic_calculus(*args):
#     return sum(args) / len(args)


# print(mid_arithmetic_calculus(2, 4, 5, 6))
# TASK TWO
# def absolute_numbr(numbr):
#     return (numbr if numbr > 0 else (numbr * -1))


# print(absolute_numbr(int(input('Enter your number: '))))
# TASK THREE

# def max_of_two(a=0, b=0):
#     return(a if a > b else b)


# print(max_of_two(268, 99599))
# TASK FOUR
def decision_on_what_to_calculate():
    try:
        calculus_decision = int(input('Choose what you wish to calculate:\n1 - for square\n2 - for triangle\n3 - for circle\n'))
        if calculus_decision == 1:
            print('You chose square')
            Square_call_answer()
        elif calculus_decision == 2:
            print('You chose triangle')
            Triangle_call_answer()
        elif calculus_decision == 3:
            print('You chose Circle')
            Circle_call_answer()
        else:
            print('You`r number is out of range, please choose one of the given.\n')
            decision_on_what_to_calculate()
    except:
        print('Wrong input')
        decision_on_what_to_calculate()


def Square_call_answer():
    try:
        height = int(input('Enter square`s height: '))
        length = int(input('Enter square`s length: '))
    except:
        print('Wrong input, please choose one of the given.\n')
        Square_call_answer()
    print('Your square`s area is: ', height * length)


def Triangle_call_answer():
    try:
        height = int(input('Enter triangle`s height: '))
        side = int(input('Enter triangle`s side length: '))
    except:
        print('Wrong input')
        Triangle_call_answer()
    print('Your triangle`s area is: ', (height * side) / 2)


def Circle_call_answer():
    Pi = 3.14
    try:
        radius = int(input('Enter circle`s radius: '))
    except:
        print('Wrong input')
        Circle_call_answer()
    print('Your circle`s area is: ', Pi * radius**2)


decision_on_what_to_calculate()
