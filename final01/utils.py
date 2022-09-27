import pandas as pd
import json
from datetime import datetime

def generate_timestamp():
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%m-%Y %H:%M:%S")
    return timestampStr

def cam_data():
    with open('json_data.json', 'r') as openfile:
        records = json.load(openfile)

    cameras = []

    for record in records:
        camera = record['camera']
        cameras.append(camera)

    sorted_cameras = sorted(list(set(cameras)))

    returned_data = []

    cameras_counts = pd.Series(cameras).value_counts()
    total_cameras = len(cameras)

    for each_camera in sorted_cameras:
        camera_count = cameras_counts.get(each_camera)
        cam_percentage = (camera_count / total_cameras) * 100
        each_cam_data = {"name": each_camera, "counts": round(cam_percentage, 2)}
        returned_data.append(each_cam_data)

    return returned_data

def yearly_data():
    with open('json_data.json', 'r') as openfile:
        records = json.load(openfile)

    years = []

    for record in records:
        year = record['timestamp'][6:10]
        years.append(year)

    sorted_years = sorted(list(set(years)))

    returned_data = {}

    years_counts = pd.Series(years).value_counts()

    for year in sorted_years:
        year_count = years_counts.get(year)
        returned_data[year] = year_count

    return returned_data

def detect_violation(number_plate):
    with open('json_data.json', 'r') as openfile:
        records = json.load(openfile)
    
    with open('violations.json', 'r') as openfile:
        violations = json.load(openfile)

    for record in records:
        if(record['license_number'] == number_plate and record['license_validity'] == False):
            violation = {
                "no": violations[-1]['no']+1,
                "license": number_plate,
                "violation": "Expired license"
            }

            violations.append(violation)

            json_string = json.dumps(violations, indent=4)

            with open('violations.json', 'w') as outfile:
                outfile.write(json_string)
