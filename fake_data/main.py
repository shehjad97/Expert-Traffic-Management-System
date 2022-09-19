import random
import string
from randomtimestamp import randomtimestamp
import json

def license_number():
    letters = string.ascii_uppercase
    digits = string.digits
    result_letters = ''.join(random.choice(letters) for i in range(3))
    result_digits = ''.join(random.choice(digits) for i in range(5))
    result = result_letters + result_digits
    return result

def timestamp():
    timestamp = randomtimestamp(start_year=2022, end_year=None, text=True)
    return timestamp

records = []

for _ in range(100):
    license_number_data = license_number()
    timestamp_data = timestamp()

    record = {
        "no": _+1,
        "license_number": license_number_data,
        "timestamp": timestamp_data
    }

    records.append(record)

# print(records)

json_string = json.dumps(records, indent=4)

with open('json_data.json', 'w') as outfile:
    outfile.write(json_string)