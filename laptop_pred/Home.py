import streamlit as st
from PIL import Image
from matplotlib import image
import os

#Title of the home page
st.header(":red[Flipkart Laptop Price Prediction Data App :desktop_computer]")
#Using subheader
st.write('By: :green[Shreyash Tare]')

#Adding Image
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_of_interest = os.path.join(FILE_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "image")
IMAGE_PATH1 = os.path.join(IMAGE_PATH, "laptop.jpg")

img = image.imread(IMAGE_PATH1)
st.image(img)

#Using markdown cell type
st.markdown(":red[Connect with me on,]")

#Creating column layout
col1,col2,col3,col4=st.columns(4, gap='small')
with col1:
    st.write("[LinkedIn](https://www.linkedin.com/in/dkteshreyashtare/)")
with col2:
    st.write("[GitHub](https://github.com/Shreyash1001)")
with col3:
    st.write("[Gmail](tareshreyash101.st@gmail.com)")
