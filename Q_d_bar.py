# # Q) d. Find distinct smdnames and calculate number of records against each and show it in
# #  a count plot
import pandas as pd
import matplotlib.pyplot as plt

information=pd.read_csv(r'C:\Users\rhutuja.b.patil\Desktop\Pandas\source.csv')
#count the smdname
uniq_org=list(information['smdName'].unique())
uniq_org_count=list(information['smdName'].value_counts())
fig, ax = plt.subplots(figsize = (19,10))
ax.barh(uniq_org,uniq_org_count)

#with the help of for loop and ax.patches method returning  unique count in smdName.
for i in ax.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.5,
            str(round((i.get_width()), 2)),
            fontsize = 10, fontweight ='bold',
            color ='black')

plt.xlabel("Count of SmdName",fontsize=20)
plt.ylabel("SmdName Name",fontsize=15)
plt.title("Count of each SmdName",y=1.05,fontsize=15);