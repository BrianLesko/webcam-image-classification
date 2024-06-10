# Brian Lesko
# 06/09/2024
# Classify Images using VGG16

import streamlit as st
import torch
import numpy as np
import torchvision.models as models # contains the the VGG16 pretrained network.
import torchvision.transforms as transforms
import cv2
from PIL import Image
import time
from customize_gui import gui

gui = gui()

gui.clean_format()
gui.about(text="In this code we will use the VGG16 model to classify images from the webcam.")

# Load the VGG16 model
model = models.vgg16(pretrained=True)

# Load ImageNet classes from a .txt file
with open('classes.txt', 'r') as f:
    imagenet_classes = [line.strip() for line in f.readlines()]

# Preprocess the image to fit the model
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])   

st.title('Image Classification with VGG16')

# Placeholders for image and predicion
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    ImageSpot = st.empty()
    Prediction = st.empty()
    TimePlaceholder = st.empty()
    Time2Placeholder = st.empty()
    Time3Placeholder = st.empty()

# Use opencv to get the current camera frame
camera = cv2.VideoCapture(0)
#camera.set(cv2.CAP_PROP_FPS, 20) # FPS
# VGA
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'YUY2')) # faster than MJPG

count=0
start_time = time.time()
while True: 
    count = count+1

    ret, frame = camera.read()
    ret, jpeg = cv2.imencode('.jpg', frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # show the image
    ImageSpot.image(frame, channels="RGB")

    time1 = time.time()
    image = Image.fromarray(frame)  # convert OpenCV image to PIL image
    image = preprocess(image)
    image = image.unsqueeze(0)  # simulate a batch
    Time2Placeholder.write(f'Preprocess Time: {time.time() - time1}')

    time1 = time.time()
    # Make a prediction
    output = model(image)
    Time3Placeholder.write(f'Prediction Time: {time.time() - time1}')

    # Interpret the output
    _, predicted_class = torch.max(output, 1)
    predicted_class = predicted_class.item()

    # Print the class name
    Prediction.write(f'Predicted class: {imagenet_classes[predicted_class]}')

    TimePlaceholder.write(f'FPS: {count/(time.time()-start_time)}')