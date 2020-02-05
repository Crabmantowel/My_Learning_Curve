ZenOfPython = """Beautiful is better than ugly.
Special cases aren\'t special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one—and preferably only one—obvious way to do it.
Although that way may not be obvious at first unless you\'re Dutch.
Now is better than never.
Although never is often better than right now
If the implementation is hard to explain, it\'s a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea—let\'s do more of those!"""

# 1)FIRST PART
Better_counter = 0
Never_counter = 0
Is_counter = 0
for i in ZenOfPython.replace('.', ' ').split():
    if i == 'better':
        Better_counter += 1
    if i == 'never':
        Never_counter += 1
    if i == 'is':
        Is_counter += 1
print("The count of word better: {Bet} \nThe count of word never: {Nev}\nThe count of word is: {Ic}".format(Bet=Better_counter, Nev=Never_counter, Ic=Is_counter))

# Another (Better?) solution:
print('The count of word better: ', ZenOfPython.count('better'))
print('The count of word never: ', ZenOfPython.count('never'))
print('The count of word is: ', ZenOfPython.count('is'))

# 2)SECOND PART
print(ZenOfPython.upper())
# 3)THIRD PART
print(ZenOfPython.replace('i', '&'))
