# Beautify Your Selfie with Eye-Closeness Estimation
This repository is built on the **pytorch [[maskrcnn_benchmark]](https://github.com/facebookresearch/maskrcnn-benchmark)**. The method is the foundation of our ReCTs-competition method [[link]](https://rrc.cvc.uab.es/?ch=12), which won the **championship**.

# Introduction
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
- python 3.8.10
- Flask 2.0.1
- gunicorn 20.1.0
- line-bot-sdk 1.8.0
- numpy 1.20.3
- pandas 1.2.4
- requests 2.25.1


## API used
- Gamil API
- Dlib Python API(Someone calls it API, and someone not)

## Enabling Gmail API

## Getting Started

- Clone this project to your local
	```bash
	$ git clone https://github.com/patty5531998/bys_sce_e_web.git
	$ cd bys_sce_e_web
	```
- Download [shape_predictor_68_face_landmarks.dat](https://drive.google.com/file/d/1EwWj7mFQqtLi_g-ZYHCc0juCWDY5FftJ/view?usp=sharing)
and uzip in ./

- fill your email@gmail.com in line34 in ./app/views.py:
  ``` bash
	our_email = 'yourmail@gmail.com'
  ```
- run the local server:
  ``` bash
	python manage.py runserver
  ```
- visit the url that the command line give you

(放圖片)



## Methods

## Results

## References

