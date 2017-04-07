'''
@Author: Shayne Zamora
@ProjectTitle: EventFinder
@Project: Used as a Google Places Command Line API Tool. Creates a Command Line Interface for Google Places.
'''

#imports and needs:
import googlemaps
import yelp
from googlemaps import places
import requests
import json, urllib
import re
from urllib import urlencode
client = googlemaps.Client(key='AIzaSyAMWWPiiqKIMReF93CjlGf2eaK6K-YMgFI')

#get user location using freegeoip.net
get_ip = 'http://freegeoip.net/json'
ip = requests.get(get_ip)
j = json.loads(ip.text)
lat = j['latitude']
lng = j['longitude']
###################
#Find places nearby
#searchRadius=raw_input('Enter the search radius in meters (must be >50,000: ')
#create request
google_request = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&keyword=cruise&key=AIzaSyAMWWPiiqKIMReF93CjlGf2eaK6K-YMgFI'
#store request
requestResults = urllib.urlopen(google_request)
#get results in json form
result = json.load(requestResults)
print result
