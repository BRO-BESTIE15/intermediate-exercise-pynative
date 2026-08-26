"""Write a function that determines if two strings are anagrams (contain the exact same characters in a different order)."""

def anagram_checker(str1, str2):
    str1 = sorted(str1.lower().replace(" ",""))
    str2 = sorted(str2.lower().replace(" ", ""))
    return str1 == str2

str1 = "silent"
str2 = "listen"
result = anagram_checker(str1, str2)
print(f"\"{str1}\" is anagram of \"{str2}\": {result}")
