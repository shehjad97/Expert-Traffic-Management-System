from datetime import datetime
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


def timestamp():
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%m-%Y %H:%M:%S")
    print(timestampStr)

###############
###############

import pandas as pd

# with open('json_data.json', 'r') as openfile:
#     records = json.load(openfile)

# # print(records[0]['timestamp'][3:5])

# months = []

# for record in records:
#     month = record['timestamp'][3:5]
#     months.append(month)

# months_counts = pd.Series(months).value_counts()

# print(months_counts.get('10'))

def get_month_count(month_str):
    with open('json_data.json', 'r') as openfile:
        records = json.load(openfile)
    
    months = []

    for record in records:
        month = record['timestamp'][3:5]
        months.append(month)

    months_counts = pd.Series(months).value_counts()
    if months_counts.get(month_str) == None:
        return 0
    else:
        return months_counts.get(month_str)

print(get_month_count('10'))
