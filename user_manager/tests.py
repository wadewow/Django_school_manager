from filecmp import cmp

from django.test import TestCase

# Create your tests here.
a = ['a', 'b', 'c']
b = [1, 2, 3]


def crossover(l1, l2):
    l3 = []
    z = list(zip(l1, l2))
    for i in z:
        for k in i:
           l3.append(k)
    return l3


c = crossover(a, b)
print(c)
