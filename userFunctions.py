#imports and needs:
import googlemaps
import requests
import json, urllib
import re
from urllib import urlencode


#Function to get IP Address
def getIPAddress():
    get_ip = 'http://freegeoip.net/json'
    ip = requests.get(get_ip)
    j = json.loads(ip.text)
    print 'Your IP Address is: ',j['ip']
#End function to get IP Address



#Search for something, the major search function
def searchForSomething():
    # get user location using freegeoip.net
    get_ip = 'http://freegeoip.net/json'
    ip = requests.get(get_ip)
    j = json.loads(ip.text)
    lat = j['latitude']
    lng = j['longitude']
    ##convert IPs to string
    userLat = str(lat)
    userLng = str(lng)

    # Get search radius from user
    print ('1. Enter a search radius in meters (must be less than 50,000): ')
    print ('WARNING: If a 0 or no number is entered it will give you the results immediately around you')
    userRadius = raw_input('Enter a search radius in meters between 0 and 50,000')
    stringRadius = getSearchRadius(userRadius)
    searchRadius = str(stringRadius)
    print searchRadius


    # try opening file for types if not close
    try:
        file = open('Types.txt')
    except:
        print IOError
    ##Display all possible types of places to search for
    for line in file:
        print line
    userType = raw_input(
        'Enter a type of place from the list above \nIf nothing is entered or not entered exactly as shown, default will be hotels nearby: ')

    ###################
    # Find places nearby
    # create request
    google_request = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + userLat + ', ' + userLng + '&radius=' + searchRadius + '&type=' + userType + '&keyword=&key=AIzaSyAMWWPiiqKIMReF93CjlGf2eaK6K-YMgFI'
    # store request
    requestResults = urllib.urlopen(google_request)
    # get results in json form
    result = json.load(requestResults)
    # print result
    # print result in nice format
    print 'Results:', '\n'
    for i in range(0, len(result['results'][0]['name'])):
        listOfItems = result['results'][i]['name']
        niceList = '\n' + listOfItems
        print niceList

#End function to search for something



#get desired radius to search to be used in search for something function
def getSearchRadius(radius):
    if(radius > 50000):
        radius = 50000
        return radius
    elif(radius < 0):
        radius = 0
        return radius
    elif(radius is ' '):
        radius = 0
        return radius
    else:
        return radius
#end searchRadius
