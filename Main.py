'''
@Author: Shayne Zamora
@ProjectTitle: EventFinder
@Project: Used as a Google Places Command Line API Tool. Creates a Command Line Interface for Google Places.
'''

#imports and needs:
import googlemaps
import requests
import json, urllib
import re
from urllib import urlencode
import userFunctions
client = googlemaps.Client(key='AIzaSyAMWWPiiqKIMReF93CjlGf2eaK6K-YMgFI')

#get user location using freegeoip.net
get_ip = 'http://freegeoip.net/json'
ip = requests.get(get_ip)
j = json.loads(ip.text)
lat = j['latitude']
lng = j['longitude']
##convert IPs to string
userLat = str(lat)
userLng = str(lng)
######################################

#Get search radius from user
print ('1. Enter a search radius in meters (must be less than 50,000): ')
print ('WARNING: If a 0 or no number is entered it will give you the results immediately around you')
userRadius = raw_input('Enter a search radius in meters between 0 and 50,000')
stringRadius = userFunctions.getSearchRadius(userRadius)
searchRadius = str(stringRadius)
print searchRadius
#######################################################################################################

#try opening file for types if not close
try:
    file = open('Types.txt')
except:
    print IOError
##Display all possible types of places to search for
for line in file:
    print line
userSelection = raw_input('Enter a type of place from the list above: ')
correctSelection = userFunctions.getUserType(userSelection)
userType = str(correctSelection)
print userType
'''
###################
#Find places nearby
#create request
google_request = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+userLat+', '+userLng+'&radius='+searchRadius+'&type='+userType+'&keyword=&key=AIzaSyAMWWPiiqKIMReF93CjlGf2eaK6K-YMgFI'
#store request
requestResults = urllib.urlopen(google_request)
#get results in json form
result = json.load(requestResults)
#print result
#print result in nice format
print 'Results:', '\n'
for i in range(0,len(result['results'][0]['name'])):
    listOfItems = result['results'][i]['name']
    niceList = '\n' + listOfItems
    print niceList
'''