import re  # Pull in Regular expressions
name = "c:\\Users\Crabmantowel\Documents\Python_projects\Thirteenth_task_file_tst.txt"
handle = open(name)
Unknown_sum = 0  # Var for summing up
for lines in handle:  # Checking each line
    checked_line = lines.rstrip()
    list_o_numbers = re.findall('[0-9]+', checked_line)  # Creating list of all numbers
    for number in list_o_numbers:  # Iterating through number list
        Unknown_sum = Unknown_sum + int(number)  # Summing everything up
print(Unknown_sum)
