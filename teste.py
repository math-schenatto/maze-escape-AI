from collections import Counter

lista = [91, 81, 71, 72, 62, 52, 53, 43, 42, 32, 31, 21, 21, 21, 2, 3, 4, 5, 6, 16, 17, 18, 28, 29, 30, 20, 10]

counter = Counter(lista)
for position in counter:
    if counter[position] > 1:
        print(counter)