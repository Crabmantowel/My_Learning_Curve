def sorter(textbooks):
    return sorted(textbooks, key=str.lower)


list_to_be_sorted = ['Alg#bra', '$istory', 'Geom^try', '**english']
print(sorter(list_to_be_sorted))
