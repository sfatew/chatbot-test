import nltk
# nltk.download('punkt')
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer(language='english')

def tokenize(s):
        return nltk.word_tokenize(s)
def stem(w):
        return stemmer.stem(w.lower())
def bag_of_words(tokenize_s,all_w):
        pass



s = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""

s=tokenize(s)
print(s)
stem_s = [stem(w) for w in s]
print(stem_s)