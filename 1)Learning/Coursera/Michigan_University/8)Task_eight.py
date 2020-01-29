fname = input("Enter file name: ")
fh = open(fname)
average_counter = 0
summed_numbers = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    average_counter = average_counter + 1
    number_start = line.find(' ')
    cut_number = float(line[number_start:])
    summed_numbers = summed_numbers + cut_number
average_number = summed_numbers / average_counter
print("Average spam confidence: ", average_number)
