#Series of n^2
list5 = []
for x in range(10):
    list5.append(x**2)
print(list5)
# list comprehension
list5 = [x**2 for x in range(10)]
print(list5)


#Series of 2n
list6 = []
for x in range(10):
    list6.append(2*x)
print(list6)
# list comprehension
list6 = [2*x for x in range(10)]
print(list6)



#Filter even numbers
list1 = [11, 22, 33, 44, 55, 66]
list2 = []
for x in list1:
    if (x % 2 == 0):
        list2.append(x)
print (list2)
# list comprehension
list2 = [x for x in list1 if (x % 2 == 0)]
print (list2)


#Flattening a list of lists
list1 = [[11, 22, 33], [44, 55, 66], [77, 88, 99]]
list2 = []
for temp_list in list1:
    for x in temp_list:
        list2.append(x)
print (list2)
# list comprehension
list2 = [x for temp_list in list1 for x in temp_list]
print (list2)



#Enlisting max() of max list
list1 = [[11,22,33],[33,44,55],[66,77,88]]
final_list = []
for temp_list in list1:
    final_list.append(max(temp_list))
print(final_list)

o = [max(temp) for temp in list1]
print(o)



#Enlisting max() of sum list
list1 = [[11,22,33],[33,44,55],[66,77,88]]
final_list = []
for n in range(len(list1)):
    list2 = [sum(x) for x in list1]
print(list2)
