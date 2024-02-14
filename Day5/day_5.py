"""
1  . Write a program that takes a number as input from the user
 and displays whether the number is even or odd.
"""
number=int(input("Enter Number :"))
if number%2==0:
    print(number," is Even.")
else:
    print(number, " Odd Number")


"""
2  . Write a program that takes a list of numbers as input from 
the user and displays the sum of all the even numbers in the list.
"""
numbers = input("Enter a list : ").split()
numbers = [int(num) for num in numbers]
print(numbers)
ev=0
for i in numbers:
    if i%2==0:
        print("Even Numbers ",i)
        ev+=i
print("Sum of Even Numbers : ",ev)

"""
3  . Write a program that displays the numbers from 1 to 10 using a for loop.
"""
for i in range(1,11):
    print(i)

"""
4  . Write a program that takes a number as input from the user and displays 
the multiplication table of the number using a while loop.
"""
i=1
multi=int(input("Enter number : "))
while i <11:
    print(multi,i,i*multi)
    i+=1

"""
5  . Write a program that takes a list of numbers as input from the user 
and displays only the odd numbers in the list using a for loop.

"""
numbers = input("Enter a list : ").split()
numbers = [int(num) for num in numbers]
print(numbers)
for i in numbers:
    if i%2!=0:
        print("Odd Numbers ",i)

"""
5.  Write a program that takes a number as input from the user and displays
 whether the number is prime or not using a try-except block.
"""
