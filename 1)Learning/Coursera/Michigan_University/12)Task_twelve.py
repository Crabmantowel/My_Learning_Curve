#  Write a program to read through the mbox-short.txt and figure out the
#  distribution by hour of the day for each of the messages. You can pull
#  the hour out from the 'From ' line by finding the time and then splitting
#  the string a second time using a colon.

#  From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#  Once you have accumulated the counts for each hour, print out the counts,
#  sorted by hour as shown below.

name = "c:\\Users\Crabmantowel\Documents\Python_projects\mbox-short.txt"
handle = open(name)
alltimestamps = []
for lines in handle:
    if not lines.startswith("From "):
        continue
    wordsInLines = lines.rstrip().split()
    fullTimeStamp = wordsInLines[5].split(':')
    alltimestamps.append(fullTimeStamp)
hoursOnlyTimestamp = []
for h, m, s in alltimestamps:
    hoursOnlyTimestamp.append(h)
hourOcurrence = dict()
for someTime in hoursOnlyTimestamp:
    hourOcurrence[someTime] = hourOcurrence.get(someTime, 0) + 1
someTup = sorted(hourOcurrence.items())
for h, v in someTup:
    print(h, v)
