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
