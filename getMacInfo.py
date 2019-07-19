#!/usr/bin/python
import requests
import sys

def getMacInfo():
    API_KEY = "at_862fgbMKpbiMK0vx2GMJrqfC6qCiU"

    MAC = sys.argv[1]
    URL = "https://api.macaddress.io/v1?apiKey=" +API_KEY+ "&output=json&search=" + MAC
    r = requests.get(URL)
    data = r.json()
    if not data['vendorDetails']['companyName']:
        print ("Vendor NOT FOUND for MAC Address "+MAC)
    else:
        print ("-----------------------------------------------------------------")
        print ("| MAC ADDRESS      | Company_Name                               |")
        print ("-----------------------------------------------------------------")
        print ("|"+MAC+" | " + data['vendorDetails']['companyName'] )
        print ("-----------------------------------------------------------------")

if __name__ == '__main__':
    getMacInfo()
