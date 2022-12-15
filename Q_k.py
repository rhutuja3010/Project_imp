#Q2 k) How many distinct titles have non-english characters?

import pandas as pd
from langdetect import detect
information = pd.read_csv('source.csv')


title=(information["title"])

English_Title=0
Non_English_Title=0

for i in title:
    if (detect(i)=="en"):
        English_Title+=1
    else:
        Non_English_Title+=1
print(" English Title Count:- ",English_Title )
print("Non English Title Count:- ",Non_English_Title)