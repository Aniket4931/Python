
"""
1 . Write a program that takes two numbers as input from the user and displays their sum.
"""
a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))
print("Sum : ",a+b)


"""
2 . Write a program that takes a string as input from the user and displays it in uppercase letters.
"""
st=input("Enter String :")
print(st.upper())


"""
3 . Write a program that displays the following text, using triple quotes:
    Programming is fun. 
    I love Python.
"""
text='''
Programming is fun. 
    I love Python.
'''
print(text)


"""
4 . Write a program that displays the following text, using escape characters:
She said, "Hello, world!"
"""
she="She said,\"Hello, world!\""
print(she)

"""
5 . Write a program that takes a sentence as input from the user and displays the number of words in the sentence.

"""
sentence = input("Enter a sentence: ")
words = sentence.split()
num_words = len(words)
print("Number of words in the sentence:", num_words)
