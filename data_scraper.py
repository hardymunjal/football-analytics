import requests
#from urllib.request import urlopen
import re # for regular expression
from bs4 import BeautifulSoup
#import urllib.parse 
import pandas as pd #importing pandas to get the data in dataframe


# request allows to get the page and read it in python.

r = requests.get("https://www.football-data.co.uk/spainm.php",headers={'User-Agent': 'Mozilla/5.0'})

#reads the cocntents of the html page
soup = BeautifulSoup(r.content, features="html.parser")

#prettifying the contents-optional
#print(soup.prettify)
   
allsearch = ''

# reading all the links on the selected page.

for link in soup.find_all('a'):
    mysearch= link.get('href')
    allsearch = allsearch+' '+mysearch

#spliting to get the array of the strings.
y = allsearch.split()
# print(y)

z = [list(x for x in y if re.search("^mmz.*.csv$",str(x)))]

#indexing to get back the list from list of list.
z=z[0]
# print(z)

#creating the base url.
base_url = 'https://www.football-data.co.uk/'

#creating an empty list to append / update with data as we read.
complete_url = []

#converting the abstract links to primary form so that they can be read.
for i in (z):
  u = base_url +  str(i) 
  complete_url.append(u)
#   print(complete_url)
  
  
"""
 using only 1st 12 years of the data from spanish soccer. The data goes back to 1992 but doen't provide much information in terms 
 of consistency with the format followed. The format changes after 2005, which is why we are selecting only 10 years data.
"""

req_url = complete_url[0:12]
print(req_url)


# # using pandas module to finally read teh data as dataframe from the links.

readings = pd.DataFrame()
for m in req_url:
    reader = pd.read_csv(m,sep=',', header=0, error_bad_lines=False)
    readings = readings.append(reader)
    # print(readings.head(n=5))

#renaming some of the column anmes as required.
readings.rename(columns={'BbMx>2.5':'BbMxTwo', 'BbAv>2.5':'BbAvTwo','BbMx<2.5':'BbMxLess','BbAv<2.5':'BbAvLess'}, inplace=True)

readings.to_csv("laliga.csv")


