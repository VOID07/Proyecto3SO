# Ecualización de una image
from numpy import asarray
import requests
import json
import base64
import time
import pathlib

ENCODING = 'ascii'
file = open(r'botnetrequests/assets/noir.jpg', 'rb')
base64_image=base64.b64encode(file.read()).decode(ENCODING)

object = {
    "image": base64_image
}
# print(object)
JSON = json.dumps(object, indent=2)
# url = 'http://localhost:7071/api/histogrameq'
# url = 'https://ddos-target-dago-2022.azurewebsites.net/api/histogrameq'

url = 'https://ddos-target-dago-2022-cons.azurewebsites.net/api/histogrameq'
start_time = time.time()

x = requests.post(url, JSON)

print("--- %s seconds ---" % (time.time() - start_time))

try:
  JSON = json.loads(x.text)
  image = JSON["image"]
  name = pathlib.Path(__file__).parent / f'botnetrequests/assets/{time.time()}.jpg'
  image_binary = base64.b64decode(image)
  image_result = open(name, 'w+b') # create a writable image and write the decoding result
  image_result.write(image_binary)

except:
  print(x.text)

