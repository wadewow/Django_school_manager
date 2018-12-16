from filecmp import cmp

from django.test import TestCase

# Create your tests here.
a = [1, 3, 5, 7]

# insert插入数据
a.insert(3, a[0])
print(a)


