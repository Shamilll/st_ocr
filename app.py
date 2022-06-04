%%writefile app.py

import streamlit as st
import numpy as np
import cv2 
import pytesseract
from PIL import Image #Python imaging library to open images

st.title('Optical Charecter recogniition (OCR)')
st.text('Upload the image')

upload_file = st.slider.fileuploadr('Choose an image',type=['jpg','png','jpeg'])
if uploaded_file is not None :   
  img = Image.open(uploaded_file)
  st.write(' ')
  if st.button('PREDICT') : 
    st.write('Result :')
    info = pytesseract.image_to_string(img) #ocr is applied using pytesseract
    st.title(info)
