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
while True:
    print ('\nDo you want to: ')
    print ('\n  1. Find your IP Address? Enter 1')
    # Begin function to obtain city
    get_ip = 'http://freegeoip.net/json'
    ip = requests.get(get_ip)
    j = json.loads(ip.text)
    city = j['city'] + ', ' + j['region_code']
    # End function to get city
    print ('\n  2. Find a place near ' + city + '? Enter 2')
    print ('\n  3. Enter the number 3 to exit the program!')
    selection = int(raw_input('\nEnter a valid value: '))
    if selection == 1:
        ##run get ip address
        userFunctions.getIPAddress()

    elif selection == 2:
        userFunctions.searchForSomething()

    elif selection == 3:
        print ('Thanks for using AroundME! ~Goodbye~')
        break
    else:
        print '\nERROR: Not a valid answer! Please enter a valid answer '

        ##TODO add functionality to see address of each place as well as possibly directions to get there
        ##TODO add the ability to only see 5-10 results
        ##TODO add a better UI system and a little more error handling
        ##TODo try to add correct functionality for the radius and other problems occured
