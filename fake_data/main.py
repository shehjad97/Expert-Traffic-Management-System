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

def get_cam():
    cam_location = "DHA"
    digits = string.digits
    result_digits = ''.join(random.choice(digits) for i in range(1))
    result = cam_location + result_digits
    return result
    # print(result)

def nid():
    digits = string.digits
    result = ''.join(random.choice(digits) for i in range(10))
    return result

def get_license_validity():
    value = [True, True, True, True, True, True, True, False]
    return random.choice(value)

def generate_fake_data():
    records = []

    for _ in range(500):
        license_number_data = license_number()
        timestamp_data = timestamp()
        cam_number = get_cam()
        nid_number = nid()
        license_validity = get_license_validity()

        record = {
            "no": _+1,
            "license_number": license_number_data,
            "nid": nid_number,
            "license_validity": license_validity,
            "camera": cam_number,
            "timestamp": timestamp_data,
        }

        records.append(record)

    json_string = json.dumps(records, indent=4)

    with open('json_data.json', 'w') as outfile:
        outfile.write(json_string)

generate_fake_data()