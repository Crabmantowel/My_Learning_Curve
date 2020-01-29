#Real task is down there
#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
largest = None #A variable to check largest value
smallest = None #A variable to check smallest value
while True: #By default always True, though the cycle will be infinite
    entered_string = input('Please type in your number: ') #Asking for input
    if entered_string == 'done': # If the input to a value is 'done' we break the loop
        break #Breaking the loop
    try:    #We try whether we can replace our "modified_string_int" with int of entered_string
        modified_string_int = int(entered_string) #replacing a str with int for comparison
    except: #If the entered_string cannot be a floating point
        print('Invalid input') # We output this string
        continue #And continue the execution of our cycle until we enter 'done' in the tab
    if smallest is None or smallest>modified_string_int: #if smallest variable is None or is bigger than next values that will be typed in
        smallest = modified_string_int # We replace the smallest variable with modified_string_int
    if largest is None or largest<modified_string_int:
        largest = modified_string_int
print("Maximum is", largest)
print("Minimum is", smallest)
