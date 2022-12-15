# Q)e. Extract list of video IDs from icarUrl field. For example, video idea in ica url 
# https://krishi.icar.gov.in/video/watch/3748 is 3748. Similarly extract all

#Importing pandas library
import pandas as pd

#Read CSV file from pandas library
information=pd.read_csv('source.csv')
# u=information["icarUrl"]
# print(u)
#Spliting string using split()
url=information["icarUrl"].str.split("/",expand=True)

# When using expand=True, the split elements will expand out into separate columns. 
# If NaN is present, it is propagated throughout the columns during the split

# print(url)
# print(len(url))
print(url[5])

# import pandas as pd
# information=pd.read_csv('source.csv')
# url=information["icarUrl"].str.split("/",expand=True)
# print(url[5])


###### or
information=pd.read_csv(r'C:\Users\rhutuja.b.patil\Desktop\Pandas\source.csv')
url=information["icarUrl"].str.split("/",expand=True)
# When using expand=True, the split elements will expand out into separate columns. 
print(url[5])
