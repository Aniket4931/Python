from my_module import square

""" 1. Write a program that defines a function to calculate the area of a rectangle. The function should take the length and width of the rectangle as input parameters and return the area."""

a1=float(input("Enter Length : "))
a2=float(input("Enter Width : "))
def calculate(length,width):
    area=length*width
    return area
area=calculate(a1,a2)
print(area)


"""
2 . Write a program that defines a function to calculate the factorial of a number. The function should take a single input parameter and return the factorial of that number.
"""

def fact(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        re=1
        for i in range(1,n+1):
            re*=i
        return re
b=fact(5)
print(b)    


"""
3 .Write a program that defines a function to calculate the sum of a list of numbers. The function should take a list of numbers as input and return the sum of those numbers.
"""
def Sum(l):
    num=0
    for i in l:
        num+=i
    return num
 
l=[4,8,5,6]
k=Sum(l)
print(k)


"""
4  .Write a program that defines a function to calculate the nth Fibonacci number. The function should take a single input parameter and return the nth Fibonacci number.
"""

def fibonaci(n):
    if n<=0:
        return None
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)
n=int(input("Enter Number : "))
a=(fibonaci(n))
print(n," Fibonacci Number ",a)

"""
5 . Create a module called my_module that defines a function to calculate the square of a number. Import the module into a new program and use the function to calculate the square of a number.
"""
a1=int(input("Enter number : "))
a=square(a1)
print("Sqare : ",a)
