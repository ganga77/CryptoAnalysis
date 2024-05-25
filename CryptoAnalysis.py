#!/usr/bin/env python
# coding: utf-8

# In[21]:


import requests
import json
import pandas as pd
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from requests import Session
from time import sleep

# Initialize the global DataFrame
df = pd.DataFrame()

#Function to call api and store it into dataframe
def api_runner():
    global df
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '15',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '28f25529-d08b-4bea-9aa8-5e64e1dfc03f',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        #print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return
    

    if 'data' in data:
        df = pd.json_normalize(data['data'])
        df['timeStamp'] = pd.to_datetime('now')

        
    if not os.path.isfile(r'/Users/gangasingh/Downloads/Crypto/API.csv'):
        df.to_csv(r'/Users/gangasingh/Downloads/Crypto/API.csv', header='column_names')
    else:
        df.to_csv(r'/Users/gangasingh/Downloads/Crypto/API.csv', mode='a', header=False)

for i in range(333):
    api_runner()
    print('API running')
    sleep(20)
exit()


# In[20]:


df


# In[24]:


pd.set_option('display.float_format', lambda x: '%.5f' % x) # rounding to 5 decimals in all columns in df


# In[28]:


df3 = df.groupby(['name'],sort=False)[['quote.USD.percent_change_1h', 'quote.USD.percent_change_24h', 'quote.USD.percent_change_7d', 'quote.USD.percent_change_30d', 'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d']].mean()


# In[29]:


df3


# In[31]:


df3.to_csv(r'/Users/gangasingh/Downloads/Crypto/Analysis.csv', sep='\t', encoding='utf-8')


# In[32]:


df3 = df3.rename(columns = {'quote.USD.percent_change_1h': '1h', 'quote.USD.percent_change_24h': '24h', 'quote.USD.percent_change_7d': '7d', 'quote.USD.percent_change_30d': '30d', 'quote.USD.percent_change_60d': '60d', 'quote.USD.percent_change_90d': '90d'})


# In[33]:


df3


# In[37]:


df3.to_excel(r'/Users/gangasingh/Downloads/Crypto/Analysis.xlsx')


# In[ ]:




