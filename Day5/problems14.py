# Problem 1
A1 = [3, 2, 6, 4, 5]
A2 = [1, 3, 2, 5]
Min=A1[0]
Max=A1[0]
Sum=0
for i in range(len(A1)):
    if A1[i]<Min:
        Min=A1[i]
    if A1[i]>Max:
        Max=A1[i]
for num in A1:
    Sum += num
ssum = (Max*(1+Max)/2)-(Min*(Min-1)/2)
if ssum == Sum:
    print(1)
else:
    print(0)

# Problem 2
number=555
k=[]
while number>0:
    d=number%10
    k.insert(0,d)
    number//=10

print(k)