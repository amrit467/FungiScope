import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import tensorflow as tf
import numpy as np

# Load the model
model = tf.keras.models.load_model('models/ringworm_detector_model.h5')

# Create the GUI
root = tk.Tk()

# Define the layout of the GUI
label = tk.Label(root, text="Fungus Image Classifier")
label.pack()

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

browse_button = tk.Button(root, text="Browse")
browse_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Define the functionality of the buttons
def browse_file():
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    img = img.resize((256, 256)) # Resize the image to match the input size of the CNN model
    img = np.array(img) / 255.0 # Normalize the pixel values
    img = np.expand_dims(img, axis=0) # Add a batch dimension
    prediction = model.predict(img)[0]
    if prediction[0] < 0.5:
           label.config(text='The image is positive for Ringworm')
    else:
        label.config(text='The image is negative for Ringworm')

browse_button.config(command=browse_file)

# Start the GUI
root.mainloop()
