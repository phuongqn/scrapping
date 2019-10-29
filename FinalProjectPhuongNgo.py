#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:54:39 2019

@author: phuongqn
"""



#get html code from url (load webpage)
from requests import get
url = 'https://www.peerspace.com/s/los-angeles/?a=photo-shoot'
response = get(url)
#Start pasring for unique tags from div and class and header
from bs4 import BeautifulSoup as bs4
html_soup = bs4(response.text, 'html.parser')
type(html_soup)
#find.all() to extract the div containers contain result
listing_containers = html_soup.find_all('div', class_ = 'Listing-Thumbnail undefined')

import csv

row_list = []
row_name = ['Description', 'Price per hour', 'Capacity', 'Review Count', 'Respond Time'] 

for detail in listing_containers:
#for loop for bs to extract data from each container in the page
        location_name = detail.h6.text
        
        price = detail.find('div', class_ = 'price-box-wrapper').text
      
        capacity = detail.find('div', class_ = 'attendee-wrapper').text
        
        review = detail.find('div', class_ = 'stars-wrapper').text
        
        responsive = detail.find('div', class_ = 'responsive-wrapper').text
#create a list of items to form information of a single location to append to row list
        row = [location_name, price, capacity, review, responsive]
        row_list.append(row)
        
with open('Results.csv', 'a') as t:
#create a csv file in the same folder in advance for simplicity and append the result to it
        writer = csv.writer(t)
        writer.writerow(row_name)
        for row in row_list:
            writer.writerow(row)
t.close()
    
    
