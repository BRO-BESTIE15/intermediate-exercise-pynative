"""Write a single-line list comprehension that takes a list of strings, filters out strings shorter than 4 characters, and converts the remaining strings to uppercase."""

words = ["apple", "bat", "cherry", "dog", "elderberry", "monkey", "boy", "lion"]

#[expression for item in iterable if condition]

filtered_words = [word.upper() for word in words if len(word)>=4]

print(filtered_words)