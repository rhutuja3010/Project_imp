# "h. What is the percentage of organization names pertaining to 'Pulses Research' against the total?"


import pandas as pd
information = pd.read_csv('source.csv')
org=information['organizationName']
pulsesandresearch=0
for i in org:
    sp=i.split()
    if "Pulses" in sp and "Research" in sp:
        pulsesandresearch+=1
print((pulsesandresearch/len(org))*100)

# ###### or
def Pulses_Percent():
  pulses_research_sum=information['organizationName'].str.findall('Pulses Research').sum()
  return "Percentage of Organization Name 'Pulses Research' against Total Organization Names:-",(len(pulses_research_sum)/len(information['organizationName']))*100 

print(Pulses_Percent())

# #### or

org=information['organizationName']
pulsesandresearch=0
for i in org:
    sp=i.split()
    if "Pulses" in sp and "Research" in sp:
        pulsesandresearch+=1
print("Percentage of Organization Name 'Pulses Research' against Total Organization Names:-",(pulsesandresearch/1000)*100)

##or ### THIS FUNTION RETURN PULSES RESEARCH SUB STRING PERCENT AGAINST TOTAL
def Pulses_Percent():

  # substring to be searched
  sub ='Pulses Research'

  ### FINDING COUNT OF SUBSTRING WITH THE HELP OF MAP AND LAMBDA FUNTION

  information['count_pulsesResearch'] = list(map(lambda x: x.count(sub), information['organizationName']))
 
  pulses_count=sum(information['count_pulsesResearch'])


  return("Percentage of Organization Name 'Pulses Research' against Total Organization Names:-",((pulses_count)/len(information['organizationName']))*100) 
print(Pulses_Percent())

# - findPercentOrgNamesPulses
# - findPercentOrgNamesPulsesAgainstResearch
# - findPercentOrgNamesResearch