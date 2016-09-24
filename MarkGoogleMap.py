#!/usr/bin/python
# 
#--------------------------------------------------------------------------------------------------
#
# Author- Prakhar Pratyush
# Desc-   Python script to mark multiple locations on the Google Map.
#
#---------------------------------------------------------------------------------------------------
#
# Acknowledgement- The original script was written by Ms. Snigdha Prakash in python 3.5 . The following 
# script is a re-implementation in Python 2.7 with subtle change and addition.
#---------------------------------------------------------------------------------------------------

import requests
import codecs
import os

#----------------------------------------------------------------------------------------------------
# Valid_Input = https://maps.googleapis.com/maps/api/geocode/outputFormat?parameters

base_url = "http://maps.googleapis.com/maps/api/geocode/json"

try:
    os.remove('Location.js')
    print('Location.js deleted successfully')
except OSError:
    pass

#def userInput():
#	location = raw_input("Enter locations: ").split()
#    return location

#def getLocation():
fileJS = codecs.open('Location.js','w', "utf-8")
fileJS.write("Location = [\n")


location = raw_input("Enter comma separated locations: ").split(',') 
#print location

for x in location:
	parameters={'address': x}
	valid_url = requests.get(base_url, params=parameters)
	data = valid_url.json()
	latitude = data["results"][0]["geometry"]["location"]["lat"]
	longitude= data["results"][0]["geometry"]["location"]["lng"]
	name = data['results'][0]['formatted_address']
	#print name, latitude, longitude
	marker="["+str(latitude)+","+str(longitude)+ ", '" +name+"']"
	print marker
	fileJS.write(marker + ",\n")
	



fileJS.write("\n];\n")
fileJS.close()
#url=requests.get(serviceurl,location[0])
#print url



