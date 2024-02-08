#1 Create a variable called "age" and assign it the value 25.
age=25
print(age)

#2 Create a variable called "name" and assign it your name as a string.
name="Aniket Patel"
print(name)

#3 Create a variable called "temperature" and assign it a float value representing the current temperature in degrees Celsius.
temperature=21.0
print(temperature)

#4 Calculate the area of a rectangle with length 5 and width 10, and assign the result to a variable called "area".
length=5
width=10
area=length*width
print("The area of the rectangle",area)

#5 Increment the value of the "age" variable by 1 using a compound assignment operator.
age=25
age+=1
print("Update age",age)

#6 Create function in python which take integer as input and convert it to binary string
def integer_to_binary(n):
    storeString = ""
    while n > 0:
        remainder = n % 2
        storeString = str(remainder) + storeString
        print(storeString)
        n //= 2
    return storeString
n = int(input("Enter Number: "))
output = integer_to_binary(n)
print("Binary :", output)


