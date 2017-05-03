#author: Shayne Zamora

#imports and needs:
import googlemaps
import requests
import json, urllib
import re


#Search for something, the major search function that searches for an item and prints the address and the Name of the place
def searchForSomething():
    # get user location using freegeoip.net
    get_ip = 'http://freegeoip.net/json'
    ip = requests.get(get_ip)
    j = json.loads(ip.text)
    lat = j['latitude']
    lng = j['longitude']
    ##convert location to string
    userLat = str(lat)
    userLng = str(lng)

    # Get search radius from user
    while True:
        try:
            print ('\nWARNING: If a 0 or no number is entered it will give you the results immediately around you and may give you 0 search results')
            print '\nRESTRICTIONS: '
            print '     Do NOT use commas'
            print '     Do NOT use decimals'
            print '     Distance is in meters'
            print '     Search radius must be between 0 (immediate results) and up to 50000'
            userRadius = raw_input('Enter a search radius in meters between 0 and 50000: ')
            intRadius = int(userRadius)
            if intRadius > 50000:
                searchRadius = '50000'
                break
            elif intRadius < 0:
                searchRadius = '0'
                break
            else:
                searchRadius = str(userRadius.strip())
                break
        except ValueError:
            print "Please enter a number without commas or decimals!"

    # try opening file for types if not close
    try:
        file = open('Types.txt')
    except:
        print IOError
    ##Display all possible types of places to search for
    for line in file:
        print line
    userAnswer = raw_input(
        'Enter a type of place from the list above: ')
    userType = userAnswer.lower()

    checkString(userType)
    while True:
        if(checkString(userType) == False):
            print 'Error, that type was not found please select from the list above: '
            userType = raw_input('Enter a type from the list above: ')
        elif(checkString(userType) == True):
            break
    showRating = False
    while True:
        try:
            print '\nWould you like to see the ratings of each place around you?'
            answer = raw_input('Enter YES or NO: ')
            userAnswer = answer.lower()
            if userAnswer == 'yes':
                showRating = True
                break
            elif userAnswer == 'no':
                break
            else:
                print 'That is not a valid answer! Try entering a valid answer'
        except ValueError:
            print 'That is not a valid answer! Try entering a valid answer'
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
        print '\nRESULTS:\n'
        for i in range(1, len(result['results'][0]['name'])):
            try:
                if i > 10:
                    print 'END OF RESULTS\n'
                    break
                elif i < 0:
                    break
                else:
                    try:
                        if showRating == True:
                            ##getting name of place
                            listOfItems = result['results'][i]['name']
                            niceList = listOfItems
                            print i,') '+'Name: ' + niceList

                            #getting address of place
                            listOfAddresses = result['results'][i]['vicinity']
                            niceAddress = listOfAddresses
                            print 'Address: '+ niceAddress

                            ##looking to see if place is open
                            listOfOpen = result['results'][0]['opening_hours']['open_now']
                            if listOfOpen == True:
                                print "It's open now! :)"
                            else:
                                print "It's closed now! :("

                            ##looking to see if place has rating, if it does, print it
                            listOfRating = result['results'][i]['rating']
                            niceRatings = listOfRating
                            print 'Rating: ' , niceRatings ,' out of 5'

                            #get user distance from each place
                            userLocation = userLat + ',' + userLng
                            Lat= result['results'][i]['geometry']['location']['lat']
                            Lng = result['results'][i]['geometry']['location']['lng']
                            destLat = str(Lat)
                            destLng = str(Lng)
                            destLocation = destLat + ',' + destLng
                            getTimeTravel(userLocation,destLocation)

                        else:
                            ##getting name of place
                            listOfItems = result['results'][i]['name']
                            niceList = listOfItems
                            print i, ') ' + 'Name: ' + niceList
                            # getting address of place

                            listOfAddresses = result['results'][i]['vicinity']
                            niceAddress = listOfAddresses
                            print 'Address: ' + niceAddress


                            ##looking to see if place is open
                            listOfOpen = result['results'][0]['opening_hours']['open_now']
                            if listOfOpen == True:
                                print "It's open now! :)"
                            else:
                                print "It's closed now! :("

                            # get user distance from each place
                            userLocation = userLat + ',' + userLng
                            Lat = result['results'][i]['geometry']['location']['lat']
                            Lng = result['results'][i]['geometry']['location']['lng']
                            destLat = str(Lat)
                            destLng = str(Lng)
                            destLocation = destLat + ',' + destLng
                            getTimeTravel(userLocation, destLocation)
########################### ERROR CATCHING ###################################################
                    except KeyError:
                        print 'Sorry, no rating available!\n'

            except IndexError:
                continue
    elif result['status'] == "ZERO_RESULTS":
            print 'No results found, try widening your radius!'
    else:
        print 'Sorry, your request was not processed successfully. Please try widening your search radius'
        return 0
#end searchForSomething


#function to check if string exists within Types.txt
def checkString(typeChoice):
    with open("Types.txt") as file:
        text = file.read().strip().split()
        while True:
            try:
                if typeChoice.lower() in text:
                    return True
                    break
                else:
                    return False
            ########################### ERROR CATCHING ################################
            except Exception as e:
                print(e)
#end checkString


# Function to get IP Address
def getIPAddress():
    get_ip = 'http://freegeoip.net/json'
    ip = requests.get(get_ip)
    j = json.loads(ip.text)
    print '\nYour IP Address is: ', j['ip']
#end getIPAddress

#get the travel distance between user and location
def getTimeTravel(start, finish):
    startLocation = start
    endLocation = finish
    distanceRequest = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=" + startLocation + "&destinations="+endLocation+"&key=AIzaSyCTr-K7HHEipMPY6UdPdVH7fd5TaBH3gLM"
    #print distanceRequest
    # store request
    timeResult = urllib.urlopen(distanceRequest)
    # distanceRequest
    results = json.load(timeResult)
    listOfTimes = results['rows'][0]['elements'][0]['distance']['text']
    niceList = listOfTimes
    print 'This location is ' + niceList + ' from you!\n'
#end getTimeTravel

#get user location
def getLocation():
    # get user location using freegeoip.net
    get_ip = 'http://freegeoip.net/json'
    ip = requests.get(get_ip)
    j = json.loads(ip.text)
    lat = j['latitude']
    lng = j['longitude']
    ##convert location to string
    userLat = str(lat)
    userLng = str(lng)
    userLocation = userLat+','+userLng
    return userLocation


#end getLocation

#begin function to get the time travel from user given destination
def getUserTimeTravel():
    try:
        while True:
            try:
                start = raw_input('\nEnter the address or place you want to start your travels.\nIf you want to use your current location, type current location: ')
                if start.__contains__(','):
                    startLocation = start.lower().replace(" ", "")
                    break
                if start.lower() == 'current location':
                    startLocation = getLocation()
                    break
                else:
                    raise ValueError
            except ValueError:
                print 'ERROR: Please enter a valid address or the words "current location"'
        while True:
            try:
                destination = raw_input('Enter the address or place of destination: ')
                if destination.__contains__(','):
                    endLocation = destination.lower().replace(" ", "")
                    break
                else:
                    raise ValueError
            except ValueError:
                print 'ERROR: Please enter a valid address'
        distanceRequest = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=" + startLocation + "&destinations=" + endLocation + "&key=AIzaSyCTr-K7HHEipMPY6UdPdVH7fd5TaBH3gLM"
        #print distanceRequest
        # store request
        timeResult = urllib.urlopen(distanceRequest)
        # distanceRequest
        results = json.load(timeResult)
        listOfTimes = results['rows'][0]['elements'][0]['duration']['text']
        niceList = listOfTimes
        print'\nRESULTS'
        getTimeTravel(startLocation,endLocation)
        print 'It will take you ' + niceList + ' to get to ' +destination+ '!\nEND RESULTS'
    except KeyError:
        print '\nERROR: Sorry there was a problem with your starting location or your endpoint\nTry entering a different address or using your current location'