#!/usr/bin/env python
# coding: utf-8

# In[109]:


import wikipediaapi
import wikipedia
import pandas as pd
import json


# In[110]:


w_page = wikipediaapi.Wikipedia(
    user_agent='docu3c (vshrav03@gmail.com)',
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)


# In[111]:


dict1 = {}
dict1["Aan Milo Sajna"] = w_page.page("Aan Milo Sajna").summary


# In[112]:


print(dict1)


# In[113]:


print(w_page.page("Aan Milo Sajna").sections)


# In[114]:


import os
current_dir = os.getcwd()
print(current_dir)


# In[115]:


os.chdir("/Users/rambo/Desktop")


# In[116]:


current_dir = os.getcwd()
print(current_dir)


# In[117]:


plot_keywords = pd.read_csv("male_adjverb.csv", on_bad_lines = 'skip')


# In[118]:


plot_keywords.head()


# In[119]:


cols = ['k1','k2','k3','k4','k5','k6','k7','k8','k9','k10',
       'k11','k12','k13','k14','k15','k16','k17','k18','k19','k20',
       'k21','k22','k23','k24','k25']

i=0
keywords=[]
while i<25:
    keywords += plot_keywords[cols[i]].values.tolist()
    i+=1


# In[120]:


len(keywords)


# In[121]:


movie_plot1 = w_page.page("Aan Milo Sajna").sections


# In[122]:


print(movie_plot1)


# In[123]:


movie_dict = {}
movie_dict['Aan Milo Sajna'] = movie_plot1

print(movie_dict)


# In[124]:


import sys
import requests
import bs4


# In[125]:


wiki_page = 'Aan Milo Sajna'
res = requests.get(f'https://en.wikipedia.org/wiki/{wiki_page}' )
res.raise_for_status()
wiki = bs4.BeautifulSoup(res.text,"html.parser")

with open(wiki_page+".txt", "w", encoding="utf-8") as f:
    for i in wiki.select('p'):
        f.write(i.getText())


# In[126]:


plot_data = pd.read_csv('male_mentions_centrality.csv', on_bad_lines='skip')


# In[127]:


plot_data.head()


# In[128]:


plot_data['MOVIE NAME'][1]


# In[129]:


len(plot_data['MOVIE NAME'])


# In[130]:


from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


# In[131]:


plot_data.shape


# In[132]:


plot_data = plot_data.dropna()


# In[133]:


plot_data['MALE CENTRIC'] = (plot_data[' AVERAGE CENTRALITY']>10)*1


# In[134]:


plot_data.head()


# In[135]:


y = plot_data['MALE CENTRIC'].copy()


# In[136]:


print(y)


# In[137]:


input_variables = ['MOVIE NAME', ' CAST', ' MENTIONS', ' TOTAL CENTRALITY', ' COUNT', ' AVERAGE CENTRALITY']
x = plot_data[input_variables].copy()


# In[138]:


x.head()


# In[139]:


y.head()


# In[143]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=300)


# In[144]:


movie_classifier = DecisionTreeClassifier(max_leaf_nodes=10, random_state=0)
movie_classifier.fit(x_train,y_train)


# In[ ]:




