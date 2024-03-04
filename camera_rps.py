import cv2
import numpy as np
from keras.models import load_model

# Load the model
model = load_model('C:/Users/waqar/Documents/GitHub/rockpaperscissorsrepository/keras_model.h5')
# Function to get the prediction
def get_prediction():
    # Open the camera
    cap = cv2.VideoCapture(0) #opens default camera
    ret, frame = cap.read() #read the camera frame
    
    # Preprocess the image
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #convert the frame from BGR to RGB
    img = cv2.resize(img, (224, 224)) #resize the image to 224x224
    img = np.expand_dims(img, axis=0) #add a batch dimension
    img = img / 255.0 #normalize the image
    
    # Get the model's prediction
    prediction = model.predict(img)[0] #get the prediction for the image
    
    # Release the camera
    cap.release() 
    
    # Return the predicted class
    classes = ['Rock', 'Paper', 'Scissors', 'Nothing']
    predicted_class = classes[np.argmax(prediction)]
    return predicted_class