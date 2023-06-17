import cv2
import numpy as np
import streamlit as st
from PIL import Image
from ultralytics import YOLO

def detect_objects(image,model):
    # Detect objects in the image
    res = model.predict(image, conf=0.3)  # conf is the confidence threshold
    res_plotted = res[0].plot()

    return res_plotted



# main function

def main():

    model = YOLO('./yolo_model.pt')

    st.title("Planets Detection")

    uploaded_files = st.file_uploader("Upload Image Files", accept_multiple_files=True)

    if st.button("Detect"):
        result_images = []

        for file in uploaded_files:
            image = Image.open(file)
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            result_image = detect_objects(image,model)
            

            # Display the result images side by side
            st.image(result_image, channels="BGR", width=400)


if __name__ == "__main__":
    main()
