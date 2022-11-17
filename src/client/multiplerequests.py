import datetime
import logging
from numpy import asarray
import requests
import json
import base64
import time
import pathlib
import os
import threading

import azure.functions as func

def postRequest(JSON):
    # url = "http://192.168.1.13:7071/api/histogrameq"
    url = "https://ddostargetdago2022.azurewebsites.net/api/histogrameq"
    while(True):
        start_time = time.time()
        try:
            requests.post(url, JSON)
        except:
            print("timeout")
            print("--- %s seconds ---" % (time.time() - start_time))

def loadBinaryAsBase64():
    # Loads image as binary
    ENCODING = 'ascii'
    name = f'botnetrequests/assets/noir.jpg'
    file = open(name, 'rb')
    base64_image=base64.b64encode(file.read()).decode(ENCODING)
    return base64_image

def createJSONFile(base64_image):
    object = {
            "image": base64_image
        }

    JSON = json.dumps(object, indent=2)
    return JSON

if __name__ == "__main__": 
    # Loads image as binary
    base64_image=loadBinaryAsBase64()

    # creates JSON object
    JSON = createJSONFile(base64_image)
    
    postRequest(JSON)
    

    
