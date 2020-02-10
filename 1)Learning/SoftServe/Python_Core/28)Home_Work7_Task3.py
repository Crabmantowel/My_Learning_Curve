def double_char(s):
    new_string = str()
    for letter in s[0:]:
        new_string += letter * 2
    return(new_string)


some_awesome_string = 'Lorem ipsum'
print(double_char(some_awesome_string))
