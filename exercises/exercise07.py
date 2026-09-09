"""Write a function to check if a full sentence is a palindrome. You must ignore case, spaces, and all punctuation marks."""

import string 



def palindrome_checker(text):
    clean = ""
    for char in text.lower():
        if char not in string.punctuation + " ":
            clean += char
    
    return clean == clean[::-1]
    

text = "A man, a plan, a canal: Panama"

print(palindrome_checker(text))