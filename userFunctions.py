#author: Shayne Zamora

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

    checkString(userType)
    while True:
        if(checkString(userType) == False):
            print 'Error, that type was not found please select from the list below: '
            for line in file:
                print line
            userType = raw_input('Enter a type from the list above: ')
        elif(checkString(userType) == True):
            break

    ###################
    # Find places nearby
    # create request
    google_request = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + userLat + ',' + userLng + '&radius=' + searchRadius + '&type=' + userType + '&keyword=&key=AIzaSyAMWWPiiqKIMReF93CjlGf2eaK6K-YMgFI'
    print google_request
    # store request
    requestResults = urllib.urlopen(google_request)
    # get results in json form
    result = json.load(requestResults)

    #checks to see if request processed successfully
    if result['status'] == "OK":
        ##TODO add functionality to only print 5-10 results
        print 'Results:', '\n'
        for i in range(1, len(result['results'][0]['name'])):
            if i > 10:
                break
            elif i < 0:
                break
            else:
                listOfItems = result['results'][i]['name']
                niceList = '\n' + listOfItems
                print niceList
    else:
        print 'Sorry, your request was not processed successfully. Please restart and try again.'
        return 0

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

def checkString(typeChoice):
    with open("Types.txt") as file:
        text = file.read().strip().split()
        while True:
            try:
                if typeChoice in text:
                    return True
                    break
                else:
                    return False
            except Exception as e:
                print(e)