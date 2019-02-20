import json

with open('ground_truth_boxes/cars.json') as f:
    gt_cars = json.load(f)
with open('ground_truth_boxes/bikes.json') as f:
    gt_bikes = json.load(f)
with open('output/cars.json') as f:
    pred_cars = json.load(f)
with open('output/bikes.json') as f:
    pred_bikes = json.load(f)

total_car_count = sum([len(boxes) for file, boxes in gt_cars.items()])
total_bike_count = sum([len(boxes) for file, boxes in gt_bikes.items()])

pred_car_count = sum(res['class'].count('car') for file, res in pred_cars.items())
pred_bike_count = sum(res['class'].count('bike') for file, res in pred_cars.items())

print(pred_car_count, pred_bike_count)
