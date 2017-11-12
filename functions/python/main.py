import json
import os

import requests

def handle(event, context):
    """
    Lambda handler
    """
    
    line_event = event['events'][0]

    if not os.environ["IFTTT_URL"]:
        return "please set IFTTT_URL"

    if line_event["type"] == "message" and line_event["message"]["type"] == "text":
        requests.post(os.environ["IFTTT_URL"], data={
            "value1": line_event["message"]["text"]
        })

    return {}
