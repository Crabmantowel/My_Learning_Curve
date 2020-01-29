#Write a program to read through the mbox-short.txt and figure out who has sent
#the greatest number of mail messages. The program looks for 'From ' lines and
#takes the second word of those lines as the person who sent the mail. The
#program creates a Python dictionary that maps the sender's mail address to a
#count of the number of times they appear in the file. After the dictionary is
#produced, the program reads through the dictionary using a maximum loop to fin
#the most prolific committer.
name = "c:\\Users\Crabmantowel\Documents\Python_projects\mbox-short.txt"
handle = open(name)
listOfAllEmails = []
for lines in handle:
    if not lines.startswith("From "):
        continue
    wordsInLines = lines.rstrip().split()
    mailWord = wordsInLines[1]
    listOfAllEmails.append(mailWord)
emailOccurence = dict()
for someEmail in listOfAllEmails:
    emailOccurence[someEmail] = emailOccurence.get(someEmail, 0) + 1
topSender = None
sendersCount = None
for emailersName, quantitySent in emailOccurence.items():
    if sendersCount is None or quantitySent > sendersCount:
        topSender = emailersName
        sendersCount = quantitySent
print(topSender, emailOccurence[topSender])
