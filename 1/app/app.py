import sys
import requests
#import numpy as np

def handler(event, context):
#    a = np.arange(15).reshape(3, 5)
#    return 'Hello from AWS Lambda using Python' + sys.version + '!' + str(a.size)
    receive = requests.get(event["url"])
    print(receive.status_code)
    print(receive.text)