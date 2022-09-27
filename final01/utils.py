import pandas as pd
import json

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