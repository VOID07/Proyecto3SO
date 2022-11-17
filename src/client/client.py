# Ecualización de una image
from numpy import asarray
import requests
import json
import base64
import time
import pathlib
import os

ENCODING = 'ascii'
file = open(r'botnetrequests/assets/boat.jpg', 'rb')
base64_image=base64.b64encode(file.read()).decode(ENCODING)

object = {
    "image": base64_image
}
# print(object)
JSON = json.dumps(object, indent=2)
# url = 'http://localhost:7071/api/histogrameq'
# url = 'https://ddos-target-dago-2022.azurewebsites.net/api/histogrameq'

url = 'https://ddostargetdago2022.azurewebsites.net/api/histogrameq'
# url = "http://192.168.1.13:7071/api/histogrameq"
print(JSON)
while(True):
  
  start_time = time.time()
  try:      
    requests.post(url, JSON)
  except:
    print("failed request")

  os.popen(f'echo {time.time() - start_time}, >> time.txt')
  print("successful request")

