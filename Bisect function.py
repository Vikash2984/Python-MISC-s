#Inserts an element at its accurate index within a sorted list
from bisect import bisect_left
from bisect import bisect_right
lst3 = [11,22,33,44,55,66]
print(bisect_left(lst3, 15),bisect_right(lst3,15))
print(bisect_left(lst3,75),bisect_right(lst3,75))
print(bisect_left(lst3,35),bisect_right(lst3,35))
print(bisect_left(lst3,44),bisect_right(lst3,44))
