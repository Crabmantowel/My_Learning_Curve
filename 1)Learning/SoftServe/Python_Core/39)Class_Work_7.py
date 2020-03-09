#TASK ONE
# try:
#     user_input = int(input("Enter your number please: "))
#     if (user_input % 2) == 0:
#         raise ValueError("Number is not dividable by 2")
# except ValueError:
#     print("Some other error occured")

# print('Final massage')

#TASK TWO
# Напишіть програму, яка пропонує користувачу ввести свій вік, після чого
# виводить повідомлення про те чи вік є парним чи непарним числом. Необхідно
# передбачити можливість введення від’ємного числа, в цьому випадку згенерувати
# власну виняткову ситуацію. Головний код має викликати функцію, яка обробляє
# введену інформацію.

# try:
#     user_age = int(input("Enter your age: "))
#     if user_age < 0:
#         raise ZeroDivisionError("Your value is less 0")
#     elif (user_age % 2) == 0:
#         print("Your age is dividable by 2, and it`s: ", user_age)
#     else:
#         print("Your age is dividable by 3, and it`s: ", user_age)
# except ValueError:
#     print("You must enter a number")
# except TypeError as t_error:
#     print(t_error)
# except NameError as n_error:
#     print(n_error)

#TASK THREE

# Напишіть програму для обчислення частки двох чисел, які вводяться користувачем
# послідовно через кому, передбачити випадок ділення на нуль, випадки
# синтаксичних помилок та випадки інших виняткових ситуацій. Використати
# блоки else та finaly.

# try:
#     num1, num2 = eval(input("Enter two numbers, separated by a comma : "))
#     result = num1 / num2
#     print("Result is", result)
# except ZeroDivisionError:
#     print("Division by zero is error !!")
# except ValueError:
#     print("Value Error.")
# except SyntaxError:
#     print("Comma is missing. Enter numbers numbers separated by comma like this 1, 2")
# except:
#     print("Wrong input")
# else:
#     print("No exceptions")
# finally:
#     print("This will execute no matter what")

#TASK FOUR

# Написати  програму, яка аналізує введене число та в залежності від числа видає
# день тижня, який відповідає цьому числу (1 це Понеділок, 2 це Вівторок і т.д.)
# Врахувати випадки введення чисел від 8 і більше, а також випадки введення не
# числових даних.

# weekdays = {1: "Monday",
#             2: "Tuesday",
#             3: "Wednesday",
#             4: "Thursday",
#             5: "Friday",
#             6: "Saturday",
#             7: "Sunday",
#             }
# try:
#     user_input = int(input("Enter number of the day: "))
#     print(weekdays[user_input])
# except KeyError:
#     print(f"There`s no {user_input}`s day in normal life")
# except ValueError:
#     print("Wrong value")
# except TypeError:
#     print("Typer error")
# finally:
#     print("I`ve ended")
