import json


def run(cars="output/cars.json", bikes="output/bikes.json", output='.'):
    with open(cars) as file:
        car_data = json.load(file)
    with open(bikes) as file:
        bike_data = json.load(file)

    # for img in car_data.keys():
    #     car_data[img]['class'] = ['car']
    # for img in bike_data.keys():
    #     bike_data[img]['class'] = ['bike']

    data = car_data

    # for img, d in bike_data.items():
    #     data[img]["boxes"] += d["boxes"]
    #     data[img]["scores"] += d["scores"]
    #     data[img]["class"] += d["class"]

    for img, d in data.items():
        lines = []
        if not d:
            continue
        for box in d:
            xmin, ymin, xmax, ymax = box
            nam = 'car'

            lines.append([nam, str(xmin), str(ymin), str(xmax), str(ymax)])

        lines_str = [" ".join(lines[i]) for i in range(len(lines))]
        lines = "\n".join(lines_str[i] for i in range(len(lines_str)))
        # print(lines)
        with open(output + '/yolo_labels/' + img[:-4] + '.txt', 'w') as label_file:
            label_file.write(lines)

    for img, d in bike_data.items():
        if not d:
            continue
        lines = []
        for box in d:
            xmin, ymin, xmax, ymax = box
            nam = 'bike'

            lines.append([nam, str(xmin), str(ymin), str(xmax), str(ymax)])

        lines_str = [" ".join(lines[i]) for i in range(len(lines))]
        lines = "\n".join(lines_str[i] for i in range(len(lines_str)))
        # print(lines)
        with open(output + '/yolo_labels/' + img[:-4] + '.txt', 'a') as label_file:
            label_file.write(lines)


if __name__ == "__main__":
    run(output='output')
