# "Search for a string [case-insensitive] in 'title' field and return count (if string found) in each distinct organization name"

import pandas as pd
information=pd.read_csv('source.csv')


def organization():
    string=(input("search the string:- ").title())

    count = information.groupby(['organizationName'])['title'].apply(lambda x: x[x.str.contains(string)].count())

    return count
print(organization())