# Problem 1
A=3
pattern = [[0] * A for k in range (A) ] 
print(pattern)

for i in range(A):
    for j in range(i+1):
        pattern[i][j]=j+1
print(pattern)

# Problem 2
# Example Input
# Input 1:
# A = [0, 2, 9]
# Input 2:
A = [5, 17, 100, 1]
max=float('-inf');
min=float('inf')
for num in A:
    if num%2==0 and num>max:
        max=num
    elif num%2!=0 and num<min:
        min=num
minmax=max-min  
print(minmax)

