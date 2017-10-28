from PyDictionary import PyDictionary
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
lmtzr = WordNetLemmatizer()
dictionary=PyDictionary()


t = ["abduction","abduction","acanthoma","achondroplasia","bactericidal","balanitis","labiodental","lactase","laparotomy"]
a = dictionary.synonym(t[0])
b = dictionary.synonym(t[1])
c = dictionary.synonym(t[2])
d = dictionary.synonym(t[3])
e = dictionary.synonym(t[4])
f = dictionary.synonym(t[5])
g = dictionary.synonym(t[6])
h = dictionary.synonym(t[7])
i = dictionary.synonym(t[8])

print("printing value:")
z = {t[0]:a,t[1]:b,t[2]:c,t[3]:d,t[4]:e,t[5]:f,t[6]:g,t[7]:h,t[8]:i}
print(z[t[0]])
print("second value")
for i in range(len(z)):
    print(z[t[i]])
