from nltk.tokenize import word_tokenize

# loading the file
filePath = 'textFile'
file = open(filePath, 'rt')
text = file.read()
file.close()

# split into words
tokens = word_tokenize(text)

print(tokens[:100])