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

# Problem 3


A = [1, 2, 2, 3, 1]
A2 = [1, 2, 2]
num = 0
for i in A2:
    num = num^i
print(num)

#problem 4
# A = [2, 4, 1, 3, 2]
# Maximum =max(A)
# Ans = 0
# for i in A:
# 	Ans += Maximum - i
# print(Ans)

def min_time_to_equality(A):
    maximum = max(A)
    ans = 0
    for i in A:
        ans += maximum - i
    return ans

# Example usage:
A = [2, 4, 1, 3, 2]
print(min_time_to_equality(A))
