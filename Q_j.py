#Qj. What is the percentage of research based organization names against total?

import pandas as pd
information= pd.read_csv('source.csv')
org=information['organizationName']
research=0
count=0

for i in org:
    sp=i.split()

    count+=1
    if "Research" in sp:
        research+=1
print(research/count*100)

####or
def Research_Percent():
  Research=information['organizationName'].str.findall('Research').sum()
  return "Percentage of Organization Name 'Research' against Total Organization Names:-",((len(Research))/len(information)*100)
print(Research_Percent())

####or

org=information['organizationName']
research=0
count=0

for i in org:
    sp=i.split()

    count+=1
    if "Research" in sp:
        research+=1
print("Percentage of Organization Name 'Research' against Total Organization Names:-",research/count*100)

####or

### THIS FUNTION RETURN  RESEARCH SUB STRING PERCENT AGAINST TOTAL
def Research_Percent():

  # substring to be searched
  sub ='Research'

  ### FINDING COUNT OF SUBSTRING WITH THE HELP OF MAP AND LAMBDA FUNTION
  research=information['count_pulsesResearch'] = list(map(lambda x: x.count(sub), information['organizationName']))

  research_count=sum(research)
  return("Percentage of Organization Name 'Research' against Total Organization Names:-",((research_count)/len(information['organizationName'])*100))

print(Research_Percent())

