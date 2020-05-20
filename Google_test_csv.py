# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:20:24 2020

@author: Hsun Jung Chen
"""

import googlemaps
import csv

#Perform request to use the Google Maps API web service
API_key = ''#enter Google Maps API key
gmaps = googlemaps.Client(key=API_key)

# 開啟 CSV 檔案
location_row = []
with open('go_track_trackspoints_csv.csv', newline='') as csvfile:

  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)

  # 以迴圈輸出每一列
  for row in rows:
#    print(row)
    location_row.append(row)
#print (location_row)


for locat in range(len(location_row)):
    if locat > 0:
#        print (location_row[locat][1],location_row[locat][2])
        
        origins = location_row[locat][1]
        destination = location_row[locat][2]
        
        directions = gmaps.directions(origins, destination,'driving')    
#        distance_result = directions[0]['legs'][0]['distance']['value']
#        duration_result = directions[0]['legs'][0]['duration']['value']        
        minute_time = duration_result = directions[0]['legs'][0]['duration']['value']/60.0   
        km_distance = directions[0]['legs'][0]['distance']['value']/1000.0
        #speed km/hr
        speed = km_distance/(minute_time/60.0)
        
        location_row[locat][4] = round(minute_time,1)
        location_row[locat][5] = round(km_distance,1)
        location_row[locat][6] = round(speed,1)
        
with open('APIs_result.csv', 'w', newline='') as csvfile:
  # 建立 CSV 檔寫入器
  writer = csv.writer(csvfile)
  for i in range(len(location_row)):
      writer.writerow(location_row[i])        
