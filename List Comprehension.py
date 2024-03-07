list5 = []
for x in range(10):
    list5.append(x**2)
print(list5)
# list comprehension
list5 = [x**2 for x in range(10)]
print(list5)



list6 = []
for x in range(10):
    list6.append(2*x)
print(list6)
# list comprehension
list6 = [2*x for x in range(10)]
print(list6)




list1 = [11, 22, 33, 44, 55, 66]
list2 = []
for x in list1:
    if (x % 2 == 0):
        list2.append(x)
print (list2)
# list comprehension
list2 = [x for x in list1 if (x % 2 == 0)]
print (list2)
