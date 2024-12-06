from collections import OrderedDict


target = 9
numbers = [2, 7, 11, 15]

freq = dict([target - x for x in numbers], range(0, len(numbers)))