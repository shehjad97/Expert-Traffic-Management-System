import json

def save_json(license_number_data):
    with open('json_data.json', 'r') as openfile:
        records = json.load(openfile)
    
    record = {
        "license_number": license_number_data
    }

    records.append(record)

    json_string = json.dumps(records, indent=4)

    with open('json_data.json', 'w') as outfile:
        outfile.write(json_string)

from datetime import datetime

def timestamp():
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%m-%Y %H:%M:%S")
    print(timestampStr)
