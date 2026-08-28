"""Given a sentence, reverse each individual word within the string while maintaining the original word order."""

def word_reverser(sentence):
    words = sentence.split(" ")
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)
    
sentence = "Python is versatile programing language"

reversed_sentence = word_reverser(sentence)
print(reversed_sentence)
