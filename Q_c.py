#Q c. Find distinct organization names and calculate number of records against each and show 
# it in a count plot
import pandas as pd
import matplotlib.pyplot as plt

information=pd.read_csv(r'C:\Users\rhutuja.b.patil\Desktop\Pandas\source.csv')

# count the organizationname
#with the help of unique() counting unique organizationName.
uniq_org=list(information['organizationName'].unique())
uniq_org_count=list(information['organizationName'].value_counts())
fig, ax = plt.subplots(figsize = (19,10))
ax.barh(uniq_org,uniq_org_count)

#with the help of for loop and ax.patches method returning  unique count in organizationName
for i in ax.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.3,
            str(round((i.get_width()), 2)),
            fontsize = 10, fontweight ='bold',
            color ='black')

plt.xlabel("Count of OrganizationName",fontsize=15)
plt.ylabel("OrganizationName Name",fontsize=15)
plt.title("Count of each OrganizationName",y=1.02,fontsize=15);