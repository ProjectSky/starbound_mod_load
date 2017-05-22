#!/usr/bin/env python3

# Created by NotePad++.
# User: Sky_Orc_Mm
# Date: 2017/5/22
# Time: 18:12
# UNIX Starbound Dedicated server mod install Script

import json
import requests

#your sbinit.config file location
CONFIG_FILE = "/home/steam/serverfiles/starbound/linux/sbinit.config"
#your WORKSHOP path
WORKSHOP_PATH = "../steamapps/workshop/content/211820/"
#get collection Info API url
STEAM_APIURL = 'http://api.steampowered.com/ISteamRemoteStorage/GetCollectionDetails/v0001/?format=json'

#get Steam workshop collection item list 
#what is collection id? ex: http://steamcommunity.com/sharedfiles/filedetails/?id=764073963
def getcollectionInfo(collection_id):
    collection = {'collectioncount': "1", 'publishedfileids[0]': collection_id}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = requests.post(STEAM_APIURL, data=collection, headers=headers)
    json_str = json.loads(data.text)
    json_data = json_str['response']['collectiondetails'][0]['children']
    return json_data

#load Config function
def loadConfig():
    with open(CONFIG_FILE, 'r') as file:
        config_data = json.load(file)
        return config_data

#save Config function
def saveConfig(config_data):
    with open(CONFIG_FILE, 'w') as config:
        json.dump(config_data, config, sort_keys=True, indent=2)

#write Config function
def writeConfig(collection_id):
    base_data = ["../assets", "../mods"]
    config_data = loadConfig()
    config_data['assetDirectories'] = []
    for key in base_data:
        config_data['assetDirectories'].append(key)
    for k in getcollectionInfo(collection_id):
            itemlist = (WORKSHOP_PATH + k['publishedfileid'])
            config_data['assetDirectories'].append(itemlist)
            saveConfig(config_data)

#write changes to sbinit.config file
writeConfig(764073963)