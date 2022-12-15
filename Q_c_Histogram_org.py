import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

information=pd.read_csv('source.csv')

store_org=list(information["organizationName"])
uniq_org=list(information["organizationName"].unique())
# print(uniq_org)

count_list=[]
for i in store_org:
	count_list.append(i)
	count = Counter(count_list)

for j in count:
	store_count=count[j]
	
fig, ax = plt.subplots(figsize = (12,5))
ax.barh(uniq_org,store_count)

# for i in ax.patches:
# # print(i)
# 	plt.text(i.get_width()+0.2, i.get_y()+0.5,
# 	str(round((i.get_width()), 2)),
# 	fontsize = 8, fontweight ='bold',
# 	color ='grey')

# plt.title('SMDNAME_VISUALIZATION', x=0.5, y=1.1,fontsize=12)
# plt.legend(bbox_to_anchor=(1.04,1), loc='upper left',title='smdName',fontsize=5)


# colors=["yellow","orange","pink","blue","red","green","brown","black","gray","violet","white"]

plt.hist(store_org,bins=store_count, orientation='horizontal')
plt.title('Organisation Name')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
# for j in count:
# 	store_count=count[j]
	
# fig, ax = plt.subplots(figsize = (12,5))
# ax.barh(uniq_org,store_count)

for i in ax.patches:
# print(i)
	plt.text(i.get_width()+0.2, i.get_y()+0.5,
	str(round((i.get_width()), 2)),
	fontsize = 8, fontweight ='bold',
	color ='grey')
plt.show()
