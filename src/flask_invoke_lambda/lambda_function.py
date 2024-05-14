import json
from datetime import datetime


def lambda_handler(event, context):
    name = event['data']['firstName']
    return {
        "statusCode": 200,
#        "headers": {
#            "Access-Control-Allow-Origin" : "*",
#            "Access-Control-Allow-Credentials" : True
#        },
        "body": json.dumps({
            "pk": event['pk'],
            "sk": event['sk'],
            "data": event['data'],
            "timenow(UTC)": datetime.now().strftime("%H:%M:%S")
        })
    }
