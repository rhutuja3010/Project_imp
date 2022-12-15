#Q b. Calculate the counts of each languages and show it in a count plot

# ### import Statement's methods
import pandas as pd
import matplotlib.pyplot as plt

# count the language
#with the help of unique() counting unique language.
information=pd.read_csv(r'C:\Users\rhutuja.b.patil\Desktop\Pandas\source.csv')
uniq_org=list(information['language'].unique())
uniq_org_count=list(information['language'].value_counts())
fig, ax = plt.subplots(figsize = (10,7))
ax.barh(uniq_org,uniq_org_count)

#with the help of for loop and ax.patches method returning unique count in language.
for i in ax.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.3,
            str(round((i.get_width()), 2)),
            fontsize = 10, fontweight ='bold',
            color ='black')

plt.xlabel("Count of Language",fontsize=15)
plt.ylabel("Language Name",fontsize=15)
plt.title("Count of each Language",y=1.02,fontsize=15);

