import os
# 1  . Write a program that opens a text file and reads the contents of the file.

file = open("c:/Users/ADMIN/OneDrive/Documents/Python/Day7/a.txt", "r")
print(file.read())


# 2  . Write a program that opens a text file and writes some text to the file.

file = open("c:/Users/ADMIN/OneDrive/Documents/Python/Day7/a.txt", "w")

file.write("Whatsapp!! Aniket")
file.close()

file = open("c:/Users/ADMIN/OneDrive/Documents/Python/Day7/a.txt", "r")
print(file.read())

# 3  . Write a program that opens a binary file and reads the first 10 bytes of the file.
fi= open("C:/Users/ADMIN/OneDrive/Documents/Python/Day7/binary_file.bin", "rb") 
first10 = fi.read(10)
print( first10)
        
# 4  .Write a program that creates a new text file, writes some text to the file, and then renames the file.
f = open("file.txt", "x")
f=open("file.txt","w")
f.write("Hello")
f.close()
s="file.txt"
r="newfile.txt"
os.rename(s,r)

# Write a program that deletes a text file.
os.remove('C:/Users/ADMIN/OneDrive/Documents/Python/Day7/k.txt')