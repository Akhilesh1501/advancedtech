# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17Q_sLP8c4pK5YOQU3qc_aXiFoITEI7_i
"""

import requests
import csv
import operator

r = requests.get('https://random-data-api.com/api/v2/users?size=2&is_xml=true').json()
  
#c = csv.writer(open("users.csv","w"), lineterminator ='\n')

c= csv.writer(open("users.csv","w"), lineterminator ='\n')  

c.writerow(  [ r[0]['id'],  r[0]['first_name'] ,  r[0]['last_name'], r[0]['username'],  r[0]['email'],   r[0]['avatar'],  r[0]['gender'] ,   r[0]['date_of_birth'] ,  ] )
c.writerow(  [ r[1]['id'],  r[1]['first_name'] ,  r[1]['last_name'], r[1]['username'],  r[1]['email'],   r[1]['avatar'],  r[1]['gender'] ,   r[1]['date_of_birth'] ,   ] )