# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:20:24 2020

@author: Hsun Jung Chen
"""

import googlemaps
import csv
import datetime
#import os

#Perform request to use the Google Maps API web service
#輸入新的金鑰
API_key = ''#enter Google Maps API key
# 連線google apis服務
gmaps = googlemaps.Client(key=API_key)

#讀取起訖點檔案
location_row = []
with open('OD_matrix.csv', newline='') as csvfile:

  rows = csv.reader(csvfile)
  for row in rows:
    location_row.append(row)

#計算所有起訖點距離時間速度
for locat in range(len(location_row)):
    if locat > 0:
#        print (location_row[locat][1],location_row[locat][2])        
        origins = location_row[locat][1] #起點
        destination = location_row[locat][2] #迄點
        
        #時間設定
        time = datetime.datetime(2020,5,23,7,0)
        tmode = 'driving'
        directions = gmaps.directions(origins, destination, mode = tmode,departure_time = time)    
        
        #時間(單位:分鐘)
        minute_time = duration_result = directions[0]['legs'][0]['duration']['value']/60.0   
        #距離(單位:公里)
        km_distance = directions[0]['legs'][0]['distance']['value']/1000.0
        #速度(單位:km/hr)
        speed = km_distance/(minute_time/60.0)
        
        location_row[locat][4] = round(minute_time,1)
        location_row[locat][5] = round(km_distance,1)
        location_row[locat][6] = round(speed,1)
        
#os.remove('APIs_result.csv')   

#寫入csv檔中
with open('OD_results.csv', 'w', newline='') as csvfile:

  writer = csv.writer(csvfile)        
  for i in range(len(location_row)):
#      print (location_row[i])
      writer.writerow(location_row[i])        
