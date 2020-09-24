##### Importing libraries and required functions #####

from nltk import ngrams
from fuzzywuzzy import fuzz

##### Creating required variables #####

stringlist = []
scorelist = []


##### Setting up review text and string value #####

text = "DON'T BUY THIS LAPTOP. THEY WILL SEND YOU A DEFECTIVE PIECE. I'M REGRETTING BIG TIME. I purchased this on 1st July 2020 and\
 within 15 days the keyboard just stopped working Engineer suspected hardware issue. I demanded replacement as for a fact they sent a defective\
 piece but amazon and lenovo both denied. Lenovo should be banned from our country. I regret for not saving enough money and buying another\
 brand. I regret I got carried away with the new launch. This laptop doesn't even deserve one star. Amazon has also lost my trust when\
 it comes to buying electronic items online. And lenovo can't even comment on their cheap quality product. DO NOT BUY.. "
 
str1 = 'keyboard stopped working'

##### Breaking text in required ngrams #####

n = 4
phrase = ngrams(text.lower().split(), n)

##### Joining n-gram tuples as strings, and then comparing with the string2  #####

for grams in phrase:
    str2 =  ' '.join(grams)
    stringlist.append(str2)
    x = fuzz.ratio(str2, str1.lower())
    scorelist.append(x)

 