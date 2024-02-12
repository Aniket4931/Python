list1=input("Enter List 1 :" )
list2=list1.split()
list1=list(list2)
print(list1)
list=len(list1)
for i in range(0,list):
    list1[i]=int(list1[i])
list1=(str(list1))
print("List 1 : ",list1)

lst2=input("(example 1 42 55 ) Enter List 2 :" )
lst3=lst2.split()
print(lst3)
lst=len(lst3)
for j in range(0,len(lst3)):
    lst3[j]=int(lst3[j])
lst3=(str(lst3))
print("List 2 ",lst3)

lst2=input("(example 1 42 55 ) Enter List 2 :" )
lst3=lst2.split()
print(lst3)
lst=len(lst3)
for j in range(0,len(lst3)):
    lst3[j]=int(lst3[j])
lst3=(str(lst3))
print("List 2 ",lst3)