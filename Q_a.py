
#Q a. Conduct a detailed analysis on missing values?

###1 FINDING NULL AND NAN VALUES
import pandas as pd
information=pd.read_csv(r'C:\Users\rhutuja.b.patil\Desktop\Pandas\source.csv')
print(information.isna().sum())
print(information.isnull().sum())