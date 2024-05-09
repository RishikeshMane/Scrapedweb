### Load Necessary Libraries
#testing
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

### Loading page content

page=requests.get('https://www.speedtest.net/global-index#mobile')
cont=page.content
print(page.status_code)
soupobj=bs(cont,'html.parser')  
#print(soupobj.prettify()) #printing out soup object 


### Data sorting
#adding all country names in empty list-empli for further data frame

countr=soupobj.find_all(class_='country')
empli=[]
for li in countr:
    empli.append(li.get_text()) 
    #print(empli)
    
#adding all internet speed rankings in empty list-empli2 for further data frame

empli2=[]
speed=soupobj.find_all(class_='speed')
for s in speed:
    empli2.append(s.get_text())
    #print(empli2)
    
### Removing Duplicates

#removing starting and ending '\n' duplicates from every item of empli. 
list3 = [x.replace('\n', '') for x in empli]  
#print(list3)

#making datfm-DataFrame
datfm=pd.DataFrame({'Countries':list3,
                    'Speed in Mbps':empli2})
                    
#Converting dataframe into csv 

datfm.to_csv('Sub.csv',index=False)

### Data  cleaning

newcsv=pd.read_csv('Sub.csv')
newcsv

Mobiletest=newcsv[1:139]  #csv for Mobile-conducted speedtest's across globe
Broadbandtest=newcsv[140:]#csv for Broadband-conducted speedtest's across globe

Mobiletest

Broadbandtest

Mobiletest.to_csv('Mobiletest.csv',index=False)
Broadbandtest.to_csv('Broadbandtest.csv',index=False)

c1=pd.read_csv('Mobiletest.csv')
c2=pd.read_csv('Broadbandtest.csv')

### Final csv's
c1.to_csv('Mobiletest.csv',index=True)
c2.to_csv('Broadbandtest.csv',index=True)
