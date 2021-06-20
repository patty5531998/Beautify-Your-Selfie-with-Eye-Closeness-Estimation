import os
from imutils import face_utils
import numpy as np
import dlib
import cv2
import glob
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# for encoding/decoding messages in base64
from base64 import urlsafe_b64decode, urlsafe_b64encode
# for dealing with attachement MIME types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from mimetypes import guess_type as guess_mime_type
import random
import string
from datetime import datetime
import shutil
# Create your views here.

our_email = 'yourmail@gmail.com'
service = build('gmail', 'v1', credentials=pickle.load(open("./token.pickle", "rb")))

def add_attachment(message, filename):
    content_type, encoding = guess_mime_type(filename)
    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
    main_type, sub_type = content_type.split('/', 1)
    if main_type == 'text':
        fp = open(filename, 'rb')
        msg = MIMEText(fp.read().decode(), _subtype=sub_type)
        fp.close()
    elif main_type == 'image':
        fp = open(filename, 'rb')
        msg = MIMEImage(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'audio':
        fp = open(filename, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=sub_type)
        fp.close()
    else:
        fp = open(filename, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()
    filename = os.path.basename(filename)
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(msg)

def build_message(destination, obj, body, attachments=[]):
    if not attachments: # no attachments given
        message = MIMEText(body)
        message['to'] = destination
        message['from'] = our_email
        message['subject'] = obj
    else:
        message = MIMEMultipart()
        message['to'] = destination
        message['from'] = our_email
        message['subject'] = obj
        message.attach(MIMEText(body))
        for filename in attachments:
            add_attachment(message, filename)
    return {'raw': urlsafe_b64encode(message.as_bytes()).decode()}

def send_message(service, destination, obj, body, attachments=[]):
    return service.users().messages().send(
      userId="me",
      body=build_message(destination, obj, body, attachments)
    ).execute()

# test send email

def index(request):
	demail = "destion mail adress"
	if request.method == "POST":
		files=[]
		location='media'

		picurl=["file1", "file2", "file3", "email"]
		# print(1)

		for i in range(4):
			if i < 3:
				files.append(request.FILES.get(picurl[i]))
			else:
				demail = request.POST.get(picurl[i])
		count = 1
		for upfile in files:
			if upfile != '':
				if not os.path.exists(location):
					os.makedirs(location)
				fss = FileSystemStorage(location=location)
				file_save = fss.save(str(count)+".jpg",upfile)
				count = count+1
		repair()

	dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	length_of_string = 6
	id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
	content = "Dear user,\nYour selfie was repaired completely.\n\nSelfie Number：" + id + "\nUpload Time：" + dt_string + "\nUser Email：" \
			  + demail + "\n\nShould you require anther set of selfies to be repaired please tell me using the following links: Welcome to Beautify Your Selfie with Eye-Closeness Estimation! - http://127.0.0.1:8000/index/"

	send_message(service, demail, "Open 24/7_No."+id,
				 content, ["./media/result.JPG"])
	shutil.rmtree('media')
	os.mkdir('media')

	return render(request, "index.html",{})


def getAreaOfPolyGonbyVector(points):

	area = 0
	for i in range(0,len(points)-1):
		p1 = points[i]
		p2 = points[i + 1]

		triArea = (p1[0]*p2[1] - p2[0]*p1[1])/2
		area += triArea

		fn=(points[-1][0]*points[0][1]-points[0][0]*points[-1][1])/2
	return abs(area+fn)

def loadImage():
	img = []
	files = glob.glob(r".\media\*")

	for fl in files:
		image = cv2.imread(fl)
		# image = cv2.resize(image, (1200, 1600),0,0, cv2.INTER_LINEAR)
		img.append(image)
	return np.array(img)

def repair():
	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor(r'.\shape_predictor_68_face_landmarks.dat')
	images = loadImage()
	Area = [[], [], []]

	list = [[[], [], [], []],
		  [[], [], [], []],
		  [[], [], [], []]]
	#image
	for r in range(len(images)):
		image = images[r]
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		rects = detector(gray, 1)

		for (i, rect) in enumerate(rects):
			count = 0
			shape = predictor(gray, rect)
			shape = face_utils.shape_to_np(shape)

			#左眼右眼
			for (name, (i, j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():
				if count == 4:
					Area[r].append(getAreaOfPolyGonbyVector(shape[i:j]))
					# print(name + str(getAreaOfPolyGonbyVector(shape[i:j])))
					(x, y, w, h) = cv2.boundingRect(np.array([shape[i:j]]))
					list[r][0].append(x-45)
					list[r][1].append(y-40)
					list[r][2].append(w+85)
					list[r][3].append(h+95)
				if count == 5:
					Area[r].append(getAreaOfPolyGonbyVector(shape[i:j]))
					# print(name + str(getAreaOfPolyGonbyVector(shape[i:j])))
					(x, y, w, h) = cv2.boundingRect(np.array([shape[i:j]]))
					list[r][0].append(x-25)
					list[r][1].append(y-50)
					list[r][2].append(w+75)
					list[r][3].append(h+95)

				count = count + 1
	n = np.array(Area)
	nT = np.transpose(n)

	index = []
	for i in range(nT.shape[0]):
		nT[i] = np.array(nT[i])
		index.append(nT[i].argmax())

	# #張數 元素數 眼鏡個數
	# #x, y, w, h
	n = np.array(list)

	for i in range(2):#眼睛
		for j in range(n[1][3][0]):#w
			images[0][n[1][1][i] + j][n[1][0][i]:n[1][0][i] + n[1][2][0]] = images[index[i]][n[1][1][i] + j][n[1][0][i]:n[1][0][i] + n[1][2][0]]

	cv2.imwrite("./media/result.JPG", images[0])