#Length of string as a list element
def myfunct(mystr):
    return len(mystr)
list1 = ['Sunday', 'Tuesday', 'Thursday', 'Saturday']
output = map(myfunct, list1)
opl = list(output)
print(list1)
print(output)
print(list(output))
print(opl[0])



#String concatination 
def myfunct2(var1,var2):
    return var1 + var2
lsit1 = ["Vikash", "Sudhanshu", "Adnan"]
list2 = ["Pandey", "Singh","Shahadat"]
o = map(myfunct2,lsit1,list2)
print(list(o))



#String -> List
def myfunct3(val):
    val.split()
i = input("Enter values : ")
temp = myfunct3(i)
o = map(split,temp)
print(list(o))
#Single insersion code
output = list(map(int,input("Enter Values : ").split()))
print(output)
