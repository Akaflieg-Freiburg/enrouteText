#!/usr/bin/python3

import json
import os.path
import requests
import sys
import xml.etree.ElementTree as ET


headers = {'Authorization': 'token {}'.format(sys.argv[1])}


# Languages and associated issue numbers are defined here

issueNumbers = {
    "de": 5,
    "es": 22,
    "fr": 7,
    "it": 16,
    "pl": 9,
    "pt": 49
    }


#
# Main program
#

for (lang, issueNumber) in issueNumbers.items():
    tree = ET.parse("assets/enroute_{}.ts".format(lang))
    root = tree.getroot()
    
    unfinished = root.findall("./context/message/translation[@type='unfinished']")

    if (len(unfinished) == 0):
        print("No missing translations in language {}. Closing the issue.".format(lang))
        payload = {'state': 'closed'}
        r = requests.post("https://api.github.com/repos/Akaflieg-Freiburg/enrouteText/issues/{}".format(issueNumber), json=payload, headers=headers)
        print(r)
    else:
        message = "There are {} unfinished translations in language {}.".format(len(unfinished), lang)
        print(message + " Opening the issue and adding a comment.")

        payload = {'state': 'open'}
        r = requests.post("https://api.github.com/repos/Akaflieg-Freiburg/enrouteText/issues/{}".format(issueNumber), json=payload, headers=headers)
        print(r)
        
        payload = {'body': message}
        r = requests.post("https://api.github.com/repos/Akaflieg-Freiburg/enrouteText/issues/{}/comments".format(issueNumber), json=payload, headers=headers)
        print(r)
