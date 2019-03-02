# import re
import string
from nltk.tokenize import word_tokenize
from nltk import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


# loading file
filePath = 'textFile'
file = open(filePath, 'rt')
text = file.read()
file.close()


# split into words by white space
# words = text.split()

# split based on words only removing punctuations.. e.g wasn't becomes wasn t
# words = re.split(r'\W+', text)

# split by whitespace and remove punctuations
# words = text.split()
#
# # remove punctuation from each word
# table = str.maketrans('', '', string.punctuation)
# stripped = [w.translate(table) for w in words]
#
# toLower = [alpha.lower() for alpha in stripped]


# split into words
tokens = word_tokenize(text)
sentence = sent_tokenize(text)

# remove all tokens that are not alphabetic
words = [word for word in tokens if word.isalpha()]

stop_words =stopwords.words('english')

# convert to lower case
tokens = [w.lower() for w in tokens]
print(tokens[:100])

# remove punctuation from each word
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
print(stripped[:100])

# remove remaining token that are not alphabetic
words = [word for word in stripped if word.isalpha()]

# filter out stop words
stp_words = set(stopwords.words('english'))
words = [w for w in words if not w in stopwords]
print(words[:100])

# stemming of words
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in tokens]


# print(tokens[:100])
# print(sentence[:100])
# print(words[:100])
# print(stop_words)
#
# print(stemmed[:100])