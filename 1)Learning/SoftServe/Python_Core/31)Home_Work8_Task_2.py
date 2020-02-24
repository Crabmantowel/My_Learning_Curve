def sorter(textbooks):
    for words in textbooks:
        textbooks[words] = words.upper() 
    pass


list_to_be_sorted = ['Alg#bra', '$istory', 'Geom^try', '**english']
print(sorter(list_to_be_sorted))
