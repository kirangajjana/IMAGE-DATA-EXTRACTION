import streamlit as st
from PIL import Image
import pytesseract

# Define the Streamlit app
st.title("Data Extraction")
st.write("Please use jpg, png images to extract the data")

# Upload an image using Streamlit's file uploader
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    # Display the uploaded image
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    # Perform OCR if the user uploads an image
    if st.button("CLICK TO EXTRACT THE DATA"):
        # Open the uploaded image
        img = Image.open(uploaded_image)

        # Perform OCR
        extracted_text = pytesseract.image_to_string(img)

        # Split the extracted text into lines
        extracted_lines = extracted_text.split("\n")

        # Display each line separately
        st.subheader("Extracted Text:")
        for line in extracted_lines:
            st.write(line)

