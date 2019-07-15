
sentence = "the woman and the children"
words = sentence.split()
print(words)
[len(word) for word in words]
print([len(word) for word in words if word != "the"])