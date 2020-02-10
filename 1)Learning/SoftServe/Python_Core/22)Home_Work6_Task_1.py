def count_positives_sum_negatives(arr):
    positives, negatives = 0, 0
    if len(arr) != 0:
        for number in arr:
            if number > 0:
                positives += 1
            else:
                negatives += number
        return [positives, negatives]
    else:
        return arr


some_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
print(count_positives_sum_negatives(some_array))
