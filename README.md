# Beautify Your Selfie with Eye-Closeness Estimation
This repository is built on the **pytorch [[maskrcnn_benchmark]](https://github.com/facebookresearch/maskrcnn-benchmark)**. The method is the foundation of our ReCTs-competition method [[link]](https://rrc.cvc.uab.es/?ch=12), which won the **championship**.

## Introduction
Beautify Your Selfie with Eye-Closeness Estimation is a system that aims to repair your eye_closeness in your selfiie. It contains two part: algorithmn to repair eye_closeness and web interface for users to use our service. 

Users who want to  use this system to make their eyes open in their selfie can easily finish the whole repair work only through the following steps:

1. upload three continuous selfies
2. leave their email address
3. press the repair button
4. check your email(the system will automatically send them a  repaired selfie)
5. done
 
web interface

We use a web as a interface to make user can upload their selfies with eye_closeness

## Prerequisites
- python == 3.7.4
- boost == 0.1
- cmake == 3.20.3
- Django == 3.2.4
- dlib == 19.22.0
- face-recognition-models == 0.3.0
- imutils == 0.5.4
- numpy == 1.16.5
- opencv-python == 4.5.2.52
- requests == 2.22.0

## API used
- Gamil API
- Dlib Python API(Someone calls it API, and someone not)

## Enabling Gmail API
1. 進入

## Getting Started

- Clone this project to your local
	```bash
	$ git clone https://github.com/patty5531998/bys_sce_e_web.git
	$ cd bys_sce_e_web
	```
- Download shape_predictor_68_face_landmarks.dat and put it in ./
Link: [[Google Drive]](https://drive.google.com/file/d/1EwWj7mFQqtLi_g-ZYHCc0juCWDY5FftJ/view?usp=sharing)

- Fill your email to our_email in line34, ./app/views.py:
  ``` bash
	our_email = 'yourmail@gmail.com'
  ```
- Run the local server:
  ``` bash
	python manage.py runserver
  ```
- Visit the url that the command line give you

(放圖片)


## Methods

## Results

* Quantitative Analysis

* Qualitative Analysis

| Scenes | Repair Rate(%)  |
|:--------:  | :-----:   |
| with glasses | 100 |
| with cap | 86.66 |
| single person | 86.66 |
| many people | 93.33 |
| indoor | 93.33 |
| outdoor | 93.33 |
| daytime | 93.33 |
| night | 86.66 |

## References
<a href="https://github.com/ultralytics/yolov5">https://github.com/ultralytics/yolov5</a>
<a href="https://github.com/ultralytics/yolov5">https://github.com/ultralytics/yolov5</a>
<a href="https://github.com/ultralytics/yolov5">https://github.com/ultralytics/yolov5</a>


