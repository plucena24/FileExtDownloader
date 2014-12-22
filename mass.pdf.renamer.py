
# coding: utf-8

# In[7]:

from BeautifulSoup import BeautifulSoup
import urllib2
import os


# In[10]:

req = urllib2.Request('http://www.cisco.com/networkers/nw04/presos/rst.html')


# In[11]:

html = urllib2.urlopen(req).read()


# In[ ]:




# In[25]:


docnames = {}
for link in soup.findAll('a'):
    try:
        if "/networkers/nw04/presos/rst_abstracts.html#" in link.get('href'):
            url, name = link.get('href').split('#')[-1], link.text
            docnames[url] = name
    except TypeError as e:
            continue
        

#for root, dirs, files in os.walk(os.curdir):
#    key = files[-4]
#    os.rename(files, str(docnames[key]))


# In[68]:

files = os.listdir(os.curdir)    

docs = {str(key[:3]+'-'+key[3:]+'.pdf'):str(val) for key, val in docnames.iteritems()}

for _file in files:
    try:
        os.rename(_file, docs[_file]+'.pdf')
    except (KeyError, ValueError) as e:
        print "{} not renamed".format(_file)
        continue
