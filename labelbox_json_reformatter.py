import json
from convert_to_yolo_format import run

with open('ground_truth_boxes/labelbox.json') as f:
    data = json.load(f)

car_output = {}
bike_output = {}

for i in data:
    car_boxes = []
    bike_boxes = []
    img = i["External ID"]
    labels = i["Label"]
    if "Car" in labels:
        for boxes in labels["Car"]:
            bboxes = boxes["geometry"]
            xmin = min([x['x'] for x in bboxes])
            ymin = min([x['y'] for x in bboxes])
            xmax = max([x['x'] for x in bboxes])
            ymax = max([x['y'] for x in bboxes])
            car_boxes.append([xmin, ymin, xmax, ymax])
    if "Bike" in labels:
        for boxes in labels["Bike"]:
            bboxes = boxes["geometry"]
            xmin = min([x['x'] for x in bboxes])
            ymin = min([x['y'] for x in bboxes])
            xmax = max([x['x'] for x in bboxes])
            ymax = max([x['y'] for x in bboxes])
            bike_boxes.append([xmin, ymin, xmax, ymax])

    car_output[img] = car_boxes
    bike_output[img] = bike_boxes

car_json = json.dumps(car_output)
bike_json = json.dumps(bike_output)
with open("ground_truth_boxes/cars.json", 'w') as f:
    f.write(car_json)
with open("ground_truth_boxes/bikes.json", 'w') as f:
    f.write(bike_json)

run(cars='ground_truth_boxes/cars.json', bikes='ground_truth_boxes/bikes.json', output='ground_truth_boxes')
