import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf

# Load the model
model = tf.keras.models.load_model('C:/Users/Laptop/models/ringworm_detector_model.h5')

# Create a Tkinter window
window = tk.Tk()

# Set the window title
window.title('Ringworm Classifier')

# Set the window size
window.geometry('500x500')

# Create a Canvas widget for the background image
canvas = tk.Canvas(window, width=window.winfo_width(), height=window.winfo_height())
canvas.pack()

# Load and resize the background image
background_image = Image.open('F:/Backlog Courses/Capstone project/hello3.jpg')  # Replace 'path_to_your_image.jpg' with the actual path to your image file
background_image = background_image.resize((window.winfo_width(), window.winfo_height()))

# Create a PhotoImage from the resized image
background_photo = ImageTk.PhotoImage(background_image)

# Set the background image on the Canvas
canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)

# Create a label for the title
title_label = tk.Label(window, text='Ringworm Classifier', font=('Arial', 20), pady=10)
title_label.pack()

# Create a label for the selected image
image_label = tk.Label(window)
image_label.pack()

# Create a label for the prediction result
result_label = tk.Label(window, font=('Arial', 16))
result_label.pack(pady=10)

# Function to browse for an image file
def browse_file():
    # Open a file dialog to browse for an image file
    filename = filedialog.askopenfilename()

    # Load the selected image using PIL
    image = Image.open(filename)

    # Resize the image to fit the label
    image = image.resize((256, 256))

    # Convert the PIL image to a numpy array
    image_array = np.array(image)

    # Scale the pixel values to be between 0 and 1
    image_array = image_array / 255.0

    # Add an extra dimension to the array to represent the batch size
    image_array = np.expand_dims(image_array, axis=0)

    # Make a prediction using the model
    prediction = model.predict(image_array)

    # Update the result label with the prediction
    if prediction[0][0] < 0.5:
        result_label.config(text='The image is positive for Ringworm')
    else:
        result_label.config(text='The image is negative for Ringworm')

    # Convert the PIL image to a Tkinter PhotoImage
    photo = ImageTk.PhotoImage(image)

    # Update the image label with the new image
    image_label.config(image=photo)
    image_label.image = photo

# Create a button to browse for an image file
browse_button = tk.Button(window, text='Browse', command=browse_file, font=('Arial', 14), padx=60, pady=10, bd=0, 
                          bg='#4CAF50', fg='white')
browse_button.pack()

# Run the Tkinter event loop
window.mainloop()
