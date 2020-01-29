#Open the file romeo.txt and read it line by line. For each line, split the line
#into a list of words using the split() method. The program should build a list of
#words. For each word on each line check to see if the word is already in the list
#and if not append it to the list. When the program completes, sort and print the
#resulting words in alphabetical order.
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    list = line.split()
    for allwords in list:
        if allwords not in lst:
            lst.append(allwords)
lst.sort() #This little shit does not need to be printed, it cannot, so just use the method to sort a list prior to printing it
print(lst)
