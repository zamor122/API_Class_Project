'''
@Author: Shayne Zamora
@ProjectTitle: AroundME!
@Project: Used as a Google Places Command Line API Tool. Creates a Command Line Interface for Google Places.
'''

#imports and needs:
import googlemaps
import requests
import json
import userFunctions
client = googlemaps.Client(key='AIzaSyAMWWPiiqKIMReF93CjlGf2eaK6K-YMgFI')

##beginning of program
print ('Welcome to AroundME! \nA program where searching is easy!')
try:
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
        print ('\n  3. Find a travel time to a destination from a start location? Enter 3')
        print ('\n  4. Enter the number 4 to exit the program!')
        try:
            selection = int(raw_input('\nEnter a valid value: '))
            if selection == 1:
                ##run get ip address
                userFunctions.getIPAddress()

            elif selection == 2:
                userFunctions.searchForSomething()

            elif selection == 3:
                userFunctions.getUserTimeTravel()
            elif selection == 4:
                print ('\nThanks for using AroundME! ~GOODBYE~')
                break
            ########################### ERROR CATCHING ################################
            else:
                print '\nERROR: Not a valid answer! Please enter a valid number '
        except ValueError:
            print '\nERROR: Not a valid answer! Please enter a valid number '
except requests.exceptions.ConnectionError:
    print '\nERROR: Cannot connect, please check your internet connection and try again'
