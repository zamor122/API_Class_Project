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


##beginning of program
print ('Welcome to AroundME \nA program where searching is easy!')
print ('\nDo you want to: ')
print ('\n  1. Find your IP Address? Enter 1')
#Begin function to obtain city
get_ip = 'http://freegeoip.net/json'
ip = requests.get(get_ip)
j = json.loads(ip.text)
city =  j['city']+', '+j['region_code']
#End function to get city
print ('\n  2.Find a place near '+city+' Enter 2')
while True:
    selection = int(raw_input('\nEnter a valid value: '))
    if selection == 1:
        ##run get ipaddress
        userFunctions.getIPAddress()
        break
    elif selection == 2:
        userFunctions.searchForSomething()
        break
    else:
        print '\nEnter a valid answer '

