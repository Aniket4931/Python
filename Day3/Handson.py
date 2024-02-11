# List Manipulation:

# Write a Python program that takes a list of integers as input and performs the following operations:
numbers=[5,6,5,78,65,25,5,4]

#  1.Remove the duplicates from the list.
print(numbers)
nu=set(numbers)
numbers=list(nu)
print("1.Remove the duplicates from the list.\n",numbers)

#  2.Sort the list in descending order.
n=len(numbers)
for i in range (n):
    for j in range(i+1,n):
        if numbers[i]<numbers[j]:
            numbers[j],numbers[i]=numbers[i],numbers[j]
print("2.Sort the list in descending order.\n",numbers)

# 3.Calculate the sum of all the elements in the list.

sum=0
for i in numbers:
    sum=sum+i
print("3.Calculate the sum of all the elements in the list.\n",sum)

# Tuple Operations:

# Create a tuple containing the names of five countries. Write a Python program that performs the following operations:
countries=("India","America","Maxico","Canada","South Africa")
print(countries)

# Check if a given country is present in the tuple.
b=("India"in countries)
print("Present in Tuple India ",b)

# Print the length of the tuple.
print("length of the tuple.",len(countries))

# Create a new tuple by concatenating the original tuple with another tuple containing five more countries.
SecondCountries=("Pakistan","Bangladesh","China","Africa","london")
print(countries.__add__(SecondCountries))

# Extra: Try modifying the element at 2nd index. What is output and why. Discuss it.
# countries[1]="Maldiv"
# print(countries)
#Tuple is immutable ,not changeable value


# Dictionary Manipulation:

# Write a Python program that operates on a dictionary representing the stock of items in a store. The dictionary should contain items as keys and their corresponding quantities as values. Perform the following operations:
container={"Pepsi":20,"Davat":10,"Coco":15}
print(dir(container))

# Add a new item to the stock.
container["RedBull"]=40
print("Add Item ",container)

# Update the quantity of an existing item.
container["Coco"]=10
print("Update item ",container)

# Remove an item from the stock.
Remove=container.pop("Pepsi")
print(Remove)
print(container)

# Print the items in stock alphabetically sorted along with their quantities.
sortAlpha=sorted(container.items())
print(sortAlpha)

# List Comprehensions:

# Write a Python program that generates a list of squares of even numbers between 1 and 20 using list comprehension.
store=[]
for num in range(1,21):
    if num %2==0:
        store.append(num**2)
print(store)

# Dictionary Iteration:

# Create a dictionary representing the population of five different cities.
City={"Ahmedabad":100,"Surat":95,"Mumbai":105,"Vadodara":65,"Botad":40}

#  Write a Python program that prints the city with the highest population along with its population.

# highest=max(City,key=City.get)   
highestCity=(max(City,key=City.get))
population=max(City.values())
print(f"{highestCity}:{population}")

# Tuple Unpacking:

# Write a Python program that takes a tuple of three integers representing the sides of a triangle as input and determines if it forms a valid triangle. If it does, print its type (equilateral, isosceles, or scalene).
a=int(input("Enter A :"))
b=int(input("Enter B :"))
c=int(input("Enter C :"))
tup=(a,b,c)
print(tup)
print(type(tup))
if a==b==c:
    print("Equilateral")
elif a==b or b==c or c==a:
    print("isosceles")
else:
    print("scalene")

# List Sorting:
    
# Write a Python program that takes a list of tuples, where each tuple contains a student's name and their score in a test. Sort the list based on the scores in descending order and print the names of the top three students.
    
students=[("Aniket",50),("Ritesh",54),("Vaibhav",52),("Sahil",74),("prahlad",65)]
sort=sorted(students,key=lambda x:x[1],reverse=True)
print(sort[0:3])

# List Manipulation:

# Write a Python program that takes a list of integers as input and performs the following operations:
lstMenu=[4,52,6,45,8,4,52,65]
print("List ",lstMenu)

# Remove the duplicates from the list.
dup=set(lstMenu)
lst=list(dup)
print("Duplicate Remove ",lst)

# Sort the list in descending order.
n=len(lst)
for i in range (n):
    for j in range(i+1,n):
        if lst[i]<lst[j]:
            lst[j],lst[i]=lst[i],lst[j]
print("Sort the list in descending order.\n",lst)

# Calculate the sum of all the elements in the list.
a=0
for k in lst:
    a+=k
print("Sum is : ",a)

# Dictionary Filtering:

# Create a dictionary representing the prices of different items in a store. Write a Python program that filters out the items with prices less than a given threshold and prints them.

store={"Bags":50.5,"Books":45.4,"Mango":26.5,"Oil":250}
threshold=int(input("Enter threshold Price "))
print("Thershould price : ",threshold)
for i ,price in store.items():
    if price<threshold:
        print(i,"Rs",price)

# List Operations:
# Write a Python program that takes two lists of integers as input and performs the following operations:

# Find the intersection of the two lists (common elements).
# Find the union of the two lists (all elements without duplicates).
# Find the elements present in the first list but not in the second list.

# list1=input("Enter List 1 :" )
# list2=list1.split()
# list1=list(list2)
# print(list1)
# list=len(list1)
# for i in range(0,list):
#     list1[i]=int(list1[i])
# list1=(str(list1))
# print("List 1 : ",list1)

# lst2=input("(example 1 42 55 ) Enter List 2 :" )
# lst3=lst2.split()
# print(lst3)
# lst=len(lst3)
# for j in range(0,len(lst3)):
#     lst3[j]=int(lst3[j])
# lst3=(str(lst3))
# print("List 2 ",lst3)

list1=[45,65,25,45,96]
list2=[78,65,45,85,73]
print(list1)
print(list2)
print("Intersection",list(set(list1)&set(list2)))
print("union",list(set(list1)|set(list2)))
print("difference first list not second list ",list(set(list1)-set(list2)))

# Dictionary Sorting:
# Write a Python program that takes a dictionary containing names as keys and their corresponding ages as values. Sort the dictionary based on ages in ascending order and print the names of the oldest and youngest person.

Dict = {"parth": 23, "temp": 24, "nikul": 18}
print(Dict)
ascending=sorted(Dict.items(),key=lambda x:x[1])
print("Ascending : ",ascending)
print("Oldest : ",ascending[-1][0])
print("youngest : ",ascending[0][0])