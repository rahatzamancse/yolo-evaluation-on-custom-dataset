# YOLO evaluation on custom dataset
> [main.ipynb](https://github.com/rahatzamancse/yolo-evaluation-on-custom-dataset/blob/master/main.ipynb)
> [DATASET](https://www.kaggle.com/insaneshadowzaman/highway-cctv-footage-images#data.zip)

This is a yolo and yolo tiny evaluation (calculating precision-recall graph and mAP) on a simple road cctv footage dataset.

See [this](https://github.com/rahatzamancse/yolo-evaluation-on-custom-dataset/blob/master/main.ipynb) for more details.
https://github.com/rahatzamancse/yolo-evaluation-on-custom-dataset/blob/master/main.ipynb

## Motivation
I have made this repository for evaluating my [this projects(traffic)](https://github.com/rahatzamancse/Traffic-Rules-Violation-Detection) model against yolo and yolo-tiny.

## Requirements
* opencv
* tqdm
* pandas
* seaborn

## Getting started
1. Download the dataset from kaggle
https://www.kaggle.com/insaneshadowzaman/highway-cctv-footage-images#data.zip
2. Just go through the main.ipynb

-------- OR --------

Use the scripts manually :
```shell
python yolo.py --images input_images --yolo yolo-coco # or --yolo yolo-tiny-coco
python convert_to_yolo_format.py
python labelbox_json_reformatter.py
python calculate_mean_ap.py
```

### Initial Configurations
Please set the model, CONFIDENCE and THRESHOLD variables in the In[2] of the main.ipynb file. All those variables are self explanatory if you are familiar with yolo models.

## Contributing
The main reason to publish something open source, is that anyone can just jump in and start contributing to my project. So If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## Links and References
Even though this information can be found inside the project on machine-readable
format like in a .json file, it's good to include a summary of most useful
links to humans using your project. You can include links like:

- Project homepage: https://github.com/rahatzamancse/yolo-evaluation-on-custom-dataset
- Repository: https://github.com/rahatzamancse/yolo-evaluation-on-custom-dataset.git
- Issue tracker: https://github.com/rahatzamancse/yolo-evaluation-on-custom-dataset
  - In case of sensitive bugs like security vulnerabilities, please contact
    rahatzamancse@gmail.com directly instead of using issue tracker. I value your effort.

## Author
Rahat Zaman
rahatzamancse@gmail.com
Student at Department of Computer Science and Engineering
Khulna University of Engineering & Technology, Khulna
Bangladesh

## Licensing
The code in this project is licensed under GNU GPLv3 license.
