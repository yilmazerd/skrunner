# This as it is can be copied to aws lambda and it runs the code provided to it

import json
import logging
import subprocess

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # TODO implement
    logger.info("Request: %s", event)
    
    f = open("/tmp/demofile2.py", "a")
    request_data_str = event["code"]
    f.write(request_data_str)
    f.close()
    
    string="python /tmp/demofile2.py"
    result=subprocess.getoutput(string)
    subprocess.getoutput("rm /tmp/demofile2.py")
    
    #return {
    #    'statusCode': 200,
    #    'body': json.dumps(result)
    #}
    return "{\body:" + result + "\}"
