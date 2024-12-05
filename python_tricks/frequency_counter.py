from collections import Counter

freq = Counter([1, 2, 4, 2, 1, 6, 6, 6])

print(list(freq.keys()))
print(list(freq.values()))

for key, value in freq.items():
    print(key, value)

for tup in freq.items():
    print(tup)

print(freq[4])




