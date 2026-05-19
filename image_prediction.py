# image_prediction.py

import streamlit as st
from PIL import Image
import torch
from torchvision import models
from torchvision.models import ResNet18_Weights

# Load Model
weights = ResNet18_Weights.DEFAULT
model = models.resnet18(weights=weights)

model.eval()

# Labels
labels = weights.meta["categories"]

# Image Transform
transform = weights.transforms()

# Streamlit UI
st.title("Simple AI Object Detector")

st.write("Upload image to detect objects.")

# Upload Image
uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

# Simplify Labels
def simplify_label(label):

    label = label.lower()

    # CAT
    if "cat" in label:
        return "Cat"

    # DOG
    elif "dog" in label:
        return "Dog"

    # HUMAN
    elif (
        "person" in label or
        "man" in label or
        "woman" in label
    ):
        return "Human"

    # CAR
    elif (
        "car" in label or
        "cab" in label or
        "jeep" in label or
        "limousine" in label or
        "wagon" in label or
        "ambulance" in label or
        "sports car" in label or
        "convertible" in label
    ):
        return "Car"

    # BIKE
    elif (
        "bicycle" in label or
        "bike" in label or
        "motorcycle" in label
    ):
        return "Bike"

    # BUS
    elif "bus" in label:
        return "Bus"

    # TRUCK
    elif "truck" in label:
        return "Truck"

    # BIRD
    elif "bird" in label:
        return "Bird"

    else:
        return label.title()

# When Image Uploaded
if uploaded_file is not None:

    # Open Image
    image = Image.open(uploaded_file).convert("RGB")

    # Display Image
    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    # Transform Image
    img_tensor = transform(image).unsqueeze(0)

    # Predict
    with torch.no_grad():
        outputs = model(img_tensor)

    # Prediction
    prediction = outputs.argmax(1).item()

    predicted_label = labels[prediction]

    # Simplified Output
    final_prediction = simplify_label(predicted_label)

    # Display Result
    st.success(f"Predicted Object: {final_prediction}")