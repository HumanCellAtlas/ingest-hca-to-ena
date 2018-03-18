import json

def convert(event, context):
    message = _process_event(event)
    response = {
        "statusCode": 200,
        "body": {}
    }
    return response

def _process_event(event):
    message = json.loads(event["body"])
    return message
    