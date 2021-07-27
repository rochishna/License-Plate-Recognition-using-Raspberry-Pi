import json
import requests
from pprint import pprint
#import picamera
import time
#camera = picamera.PiCamera()
r="123.jpg"
#camera.capture(r)
#camera.close()
regions = ['gb', 'it']
with open(r, 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': ''})
#print(response.json())
l=response.json()
l=l['results']
l=str(l).split(":")
l=l[6].split(',')
l=l[0]
l=l.split(' ')
l=l[1].replace("'",'')
print(l)
