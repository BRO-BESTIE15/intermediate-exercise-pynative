"""Given a list of strings, use a single list comprehension to extract strings that meet two criteria: they must be longer than 5 characters AND they must start with a vowel (a, e, i, o, u)."""

vowels = "aeiou"

words = [
"sunflower",
"crystal",
"penguin",
"apple",
"river",
"cloud",
"stone",
"alphabet",
"icecream"
]

filtered_words = [
word 
for word in words 
if len(word) > 5 
and 
word[0].lower() in vowels
]

print(filtered_words)