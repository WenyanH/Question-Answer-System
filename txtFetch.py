
# coding: utf-8

# In[7]:

import urllib
from bs4 import BeautifulSoup
import sys
sys.argv  
cmdargs=list(sys.argv)
url=""
url=cmdargs[1]
#html=urllib.urlopen("https://en.wikipedia.org/wiki/Spanish_language").read()
html=urllib.urlopen(url).read()
soup=BeautifulSoup(html)
text=""
text=soup.body.get_text()
print text

