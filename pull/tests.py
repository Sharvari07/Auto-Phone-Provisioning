from django.test import TestCase
import dateutil.parser


""" b = '2019-07-23T16:24:12-03:00'

c = (b[0:19])
print(c)
a = dateutil.parser.parse(c)
print(a)  """
# Create your tests here.

a = [1,3,4,5,6,7,3,3,4,5,2,3,3,3,3,3]

j = 0 

for i in a:
    if i == 3:
        print(i)
        j = j + 1
    if j == 5:
        break