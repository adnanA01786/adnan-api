# -*- coding: utf-8 -*-

import json
import os
import string
import io


JSON_FILE    = 'returnfile.json'
API_VERSION  = '1.0'


# Return API Version Information
def getAPIVersion():
    return API_VERSION

# checks if str2 is present in str1 
# returns a bool
# note: no error handling is present in this
#       method
def checkCommand(str1, str2):
    return str1.split(str2)[1]

# Check if a given input integer digit is a
# multiple of mult
# note: no error handling is present in this
#       method
def isMultiple(digit, mult):
    return (digit % mult) == 0

# Calculates the return value
# note: No error handling
# TO#DO: API should incorporate error
# handling rather than server code 
def calculateReturn(digit):

    mult7 = isMultiple(digit, 7)
    mult9 = isMultiple(digit, 9)

    if mult7 and mult9:
        return "SN"
    elif mult7:
        return "S"
    elif mult9:
        return "N"
    else:
        # Not a multiple of either numbers
        return digit

# Construct a file with a json response and send that
# note: this is deprecated 
def constructResponse(value):
    try:
        file = open(JSON_FILE,'w') 
        file.write(json.dumps({'Response':value, 'API Version': '1.0' }, sort_keys=True, 
            indent=4, separators=(',', ': ')))
        file.close()
        return JSON_FILE
    except:
        return None

# Return a json string for streaming rather than returning a client
# supersedes constructResponse
def constructResponse2(value):
    return json.dumps({'Response':value, 'API Version': '1.0' }, sort_keys=True, 
            indent=4, separators=(',', ': '))

# A main for testing individual bits of the API
def main():
    json_response = constructResponse(calculateReturn(14))
    print(json_response)


if __name__ == "__main__":
    main()
