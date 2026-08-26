"""Create a function that takes a string and returns a count of how many times each character appears. Ignore spaces and make it case-insensitive."""
from collections import Counter
def char_counter(string):
    clean_string = string.lower().replace(" ", "")
    count = Counter(clean_string)
    return count 

string = "Is your code pythonic?"
print(char_counter(string))