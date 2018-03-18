import json


def handle(event, context):
    _process_event(event)
    response = {
        "statusCode": 200,
        "body": {}
    }
    return response


def convert(dataset_json):
    for element in dataset_json:
        if 'schema_type' in element:
            print(element['schema_type'])


def _process_event(event):
    submission = json.loads(event["body"][0])
    return submission
