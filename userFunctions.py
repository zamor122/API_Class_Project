#imports and needs:
import googlemaps
import requests
import json, urllib
import re
import mmap
from urllib import urlencode


#get desired radius to search
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


#get user search type
def getUserType(userType):
    #try opening file for types if not close
    try:
        file = open('Types.txt')
    except:
        print IOError
    #check if user type is valid
    for line in file:
        if userType in file:
            if re.search("\b{0}\b".format(userType),line):
                print line
        else:
            print 'Your type was not valid, please enter another type'
            userType = raw_input('Enter another type: ')