import logging
import matplotlib.pyplot as plt
import numpy as np
from numpy import asarray
import json
from json import JSONEncoder
import time
import base64
from PIL import Image  
import azure.functions as func
import os

def histogram(p_image):
    ENCODING = 'utf-8'
    # Load list as numpy array to process the image
    A = np.uint8(asarray(p_image))
    h = np.histogram(A, bins=256, range=(0,255))[0] # Cálculo de histograma
    # Calculete max and min to perform the stretch
    r_min = np.min(A)
    r_max = np.max(A)

    # Estiramiento del histograma
    B = np.uint8((A-r_min)/(r_max-r_min)*255)
    B = B.tolist()
    plt.imshow(B)
    name = f'/tmp/images/{time.time()}.jpg'
    plt.imsave(f'{name}', B, cmap='gray')

    file = open(name, 'rb')
    bytes = base64.b64encode(file.read()).decode(ENCODING)
    return bytes


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    image = req.params.get('image')
    if not image:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            image = req_body.get('image')

    if image:

        # Decode bas64 image to binaries
        # Save image as a file in the FS
        # folder = r'/tmp/images'
        # os.makedirs(folder, exist_ok=True)
        # name =  f'/tmp/images/{time.time()}.jpg'
        name =  f'/images/{time.time()}.jpg'
        image_result = open(name, 'w+b') # create a writable image and write the decoding result
        image_binary = base64.b64decode(image)
        image_result.write(image_binary)
        
        # # Opens the file as an image
        img_arr=Image.open(name).convert('L')
        img_arr = np.asarray(img_arr)

        # Perform histogram stretch
        image2 = histogram(img_arr)

        object = {
            "image": image2
        }

        dump = json.dumps(object)
        return func.HttpResponse(dump)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass an image to execute successfully",
             status_code=200
        )
