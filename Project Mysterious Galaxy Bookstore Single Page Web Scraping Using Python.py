#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib
 


# In[2]:


#Connect to Website

URL = 'https://www.mystgalaxy.com/book/9781250878533'

headers = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0")

page = requests.get(URL, headers+headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

print(soup2)




# In[ ]:





# In[3]:


title = soup2.find("h1", {"class" :"page-title"}).get_text()

print(title)


# In[ ]:





# In[4]:


price = soup2.find("div", {"class": "abaproduct-price"}).get_text()


print(price)


# In[ ]:





# In[5]:


print(title)
print(price)


# In[6]:


price = price.strip()[1:]
title = title.strip()

print(title)
print(price)


# In[7]:


import datetime

today = datetime.date.today()

print(today)


# In[8]:


type(title)
type(price)


# In[9]:


import csv

header = ['Title', 'Price', 'Date']

data = [title, price, today]

type(data)



# In[10]:


import csv

with open("MysteriousGalaxyKaijuScraperDataSet.csv" , 'w', newline="", encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[ ]:





# In[11]:


#Now we are appending data to the csv

with open("MysteriousGalaxyKaijuScraperDataSet.csv" , 'a+', newline="", encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[12]:


import pandas as pd

df = pd.read_csv(r'C:\Users\Owner\MysteriousGalaxyKaijuScraperDataSet.csv')

print(df)


# In[18]:


def check_price():

    URL = 'https://www.mystgalaxy.com/book/9781250878533'

    headers = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0")

    page = requests.get(URL, headers+headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
    
    title = soup2.find("h1", {"class" :"page-title"}).get_text()
    
    price = soup2.find("div", {"class": "abaproduct-price"}).get_text()
    
    price = price.strip()[1:]
    title = title.strip()
    
    import datetime

    today = datetime.date.today()
    
    import csv

    header = ['Title', 'Price', 'Date']

    data = [title, price, today]
    
    with open("MysteriousGalaxyKaijuScraperDataSet.csv" , 'a+', newline="", encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)


# In[ ]:


while(True):
    check_price()
    time.sleep(86400)   
if (price <= 14):
    send_mail()


# In[ ]:


import pandas as pd

kaiju = pd.read_csv(r'C:\Users\Owner\MysteriousGalaxyKaijuScraperDataSet.csv')

print(kaiju)


# In[ ]:





# In[ ]:


def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('Tikva.A.Cohen@gmail.com', 'XXXXXX')
    
    subject = "Book on Sale!"
    body = "Tikva, the book you wanted 'The Kaiju Preservation Society' is NOW ON SALE at Mysterious Galaxy!"
    
      msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'Tikva.A.Cohen@gmail.com',
        msg
     
    )
    
    


# In[ ]:




