import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load the trained model
model = tf.keras.models.load_model('currency_detector.h5')

# Define class names based on the dataset
class_names = ['100', '500', '1000', 'fake 100', 'fake 500']

# Prediction function
def predict(image):
    # Preprocess the image to match model input requirements
    image = image.resize((224, 224))  # Resize to 224x224 pixels
    image = np.array(image) / 255.0   # Normalize pixel values to [0, 1]
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    # Make prediction
    prediction = model.predict(image)
    class_idx = np.argmax(prediction)  # Get the index of the highest probability
    confidence = np.max(prediction) * 100  # Convert to percentage
    return class_names[class_idx], confidence

# Streamlit interface
st.title("Nepali Currency Detector")
st.write("Upload an image of a Nepali currency note to determine if it's real or fake.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Predict and display result
    label, confidence = predict(image)

    # Determine if the currency is real or fake
    if 'fake' in label:
        result = "Fake Currency"
    else:
        result = "Real Currency"

    # Display the result in a clear format
    st.subheader("Detection Result")
    st.write(f"**Status**: {result}")
    st.write(f"**Confidence**: {confidence:.2f}%")

st.write("**Note**: This app detects whether the uploaded Nepali currency note is real or fake.")