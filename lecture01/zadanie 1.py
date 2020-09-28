from math import cos
from math import sqrt
from math import radians
a = float(input())
b = float(input())
c = float(radians(float((input()))))
d =float(sqrt(a*a+b*b-2*a*b*cos(c)))
print(d)