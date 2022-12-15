# f. Search for a string [case-insensitive] in 'keywords' field and return count
#  (if string found) in each distinct organization name



import pandas as pd
 
information=pd.read_csv('source.csv')

count = information.groupby(['organizationName'])['keywords'].apply(lambda x: x[x.str.contains('Amrut|Amrit|Paddy')].count())

print(count)



def organization():
    string=(input("search for string:- ").title())

    count = information.groupby(['organizationName'])['keywords'].apply(lambda x: x[x.str.contains(string)].count())

    return count
print(organization())
