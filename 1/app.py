import os
import json
import requests
import logging

def handler(event, context):

    url = event['url']
    r = requests.get(url)
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info(r.status_code)


    return {
        "status code": r.status_code
    }