# python 3+ required
import csv
from collections import Counter

# if numbers = 10, we will print the most successful 10 numbers.
def loto(file, numbers=None):

    with open(file, 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        your_list.pop(0)
        for i in your_list:
            for j in range(len(i)):
                if j == 0:
                    i.pop(j)

    flattened_list = [elem for sublist in your_list for elem in sublist if elem != '']

    counter = Counter(flattened_list)
    for i in counter.most_common(numbers):
        print (i[0], end=' ')
        # i[0] -- number, i[1] -- number_counter

sum = 0;
print("5/40:")
loto("540.csv")
print("\n6/49:")
loto("loto649.csv")
print('\n')
