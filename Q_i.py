# # i. What is the percentage of organization names pertaining to 'Pulses Research' against
# #    the general 'research' oriented organization names?


import pandas as pd

information = pd.read_csv('source.csv')
org=information["organizationName"]
pulsesandresearch=0
research=0
for i in org:
    sp=i.split()
    if "Pulses" in sp and "Research" in sp:
        pulsesandresearch+=1
    if "Research" in sp:
        research+=1
print(pulsesandresearch/research*100)



###or

def PulsesResearch_Percent():
  Pulses=information['organizationName'].str.findall('Pulses Research').sum()
  Research=information['organizationName'].str.findall('Research').sum()
  return "Percentage of Organization Name 'Pulses Research' against Organization Name  'Research' is:-",(((len(Pulses))*100)/len(Research))

print(PulsesResearch_Percent())

###or

org=information["organizationName"]
pulsesandresearch=0
research=0
for i in org:
    sp=i.split()
    if "Pulses" in sp and "Research" in sp:
        pulsesandresearch+=1
    if "Research" in sp:
        research+=1
print("Percentage of Organization Name 'Pulses Research' against Organization Name  'Research' is:-",(pulsesandresearch/research)*100)


###or

### THIS FUNTION RETURN  RESEARCH SUB STRING PERCENT AGAINST TOTAL
def PulsesResearch_Percent():

  # substring to be searched
  sub ='Research'
  sub1 ='Pulses Research'

  ### FINDING COUNT OF SUBSTRING WITH THE HELP OF MAP AND LAMBDA FUNTION
  pulses=information['count_pulsesResearch'] = list(map(lambda x: x.count(sub1), information['organizationName']))
  research=information['count_pulsesResearch'] = list(map(lambda x: x.count(sub), information['organizationName']))
 
  pulses_count=sum(pulses)
  research_count=sum(research)
  return("Percentage of Organization Name 'Pulses Research' against Organization Name  'Research' is:-",(((pulses_count)/(research_count))*100))

print(PulsesResearch_Percent())