import streamlit as st
import numpy as np
from detect import predict
from PIL import Image

def detect_objects(image_file):
    img = Image.open(image_file)
    img_array = np.array(img)
    predicted_image = predict(img_array)

    return predicted_image

def main():
    st.subheader("Detection in Photo")
    tab1, tab2 = st.tabs(["Upload picture", "Take picture"])

    with tab1:
        uploaded_file = st.file_uploader("Choose an image file", type=['jpg', 'png'])
        if uploaded_file is not None:
            st.image(detect_objects(uploaded_file))

    with tab2:
        picture = st.camera_input("Take a photo to detect objects within it.")
        if picture:
            st.image(detect_objects(picture))

if __name__=="__main__":
    main()