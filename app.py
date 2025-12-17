from __future__ import division, print_function
import sys
import os
import glob
import re
import numpy as np
import tensorflow as tf
import cv2

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from flask import Flask, redirect, url_for, request, render_template, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

MODEL_PATH ='model.h5'

model = load_model(MODEL_PATH)

def grayscale(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return img
def equalize(img):
    img =cv2.equalizeHist(img)
    return img
def preprocessing(img):
    img = grayscale(img)
    img = equalize(img)
    img = img/255
    return img
def getClassName(classNo):
    if   classNo == 0: return 'Speed Limit 20 km/h'
    elif classNo == 1: return 'Speed Limit 30 km/h'
    elif classNo == 2: return 'Speed Limit 50 km/h'
    elif classNo == 3: return 'Speed Limit 60 km/h'
    elif classNo == 4: return 'Speed Limit 70 km/h'
    elif classNo == 5: return 'Speed Limit 80 km/h'
    elif classNo == 6: return 'End of Speed Limit 80 km/h'
    elif classNo == 7: return 'Speed Limit 100 km/h'
    elif classNo == 8: return 'Speed Limit 120 km/h'
    elif classNo == 9: return 'No passing'
    elif classNo == 10: return 'No passing for vechiles over 3.5 metric tons'
    elif classNo == 11: return 'Right-of-way at the next intersection'
    elif classNo == 12: return 'Priority road'
    elif classNo == 13: return 'Yield'
    elif classNo == 14: return 'Stop'
    elif classNo == 15: return 'No vechiles'
    elif classNo == 16: return 'Vechiles over 3.5 metric tons prohibited'
    elif classNo == 17: return 'No entry'
    elif classNo == 18: return 'General caution'
    elif classNo == 19: return 'Dangerous curve to the left'
    elif classNo == 20: return 'Dangerous curve to the right'
    elif classNo == 21: return 'Double curve'
    elif classNo == 22: return 'Bumpy road'
    elif classNo == 23: return 'Slippery road'
    elif classNo == 24: return 'Road narrows on the right'
    elif classNo == 25: return 'Road work'
    elif classNo == 26: return 'Traffic signals'
    elif classNo == 27: return 'Pedestrians'
    elif classNo == 28: return 'Children crossing'
    elif classNo == 29: return 'Bicycles crossing'
    elif classNo == 30: return 'Beware of ice/snow'
    elif classNo == 31: return 'Wild animals crossing'
    elif classNo == 32: return 'End of all speed and passing limits'
    elif classNo == 33: return 'Turn right ahead'
    elif classNo == 34: return 'Turn left ahead'
    elif classNo == 35: return 'Ahead only'
    elif classNo == 36: return 'Go straight or right'
    elif classNo == 37: return 'Go straight or left'
    elif classNo == 38: return 'Keep right'
    elif classNo == 39: return 'Keep left'
    elif classNo == 40: return 'Roundabout mandatory'
    elif classNo == 41: return 'End of no passing'
    elif classNo == 42: return 'End of no passing by vechiles over 3.5 metric tons'


def model_predict(img_path, model):
    print(img_path)
    img = image.load_img(img_path, target_size=(224, 224))
    img = np.asarray(img)
    img = cv2.resize(img, (32, 32))
    img = preprocessing(img)
    # Removed cv2.imshow() as it causes issues in web app context
    img = img.reshape(1, 32, 32, 1)
    # PREDICT IMAGE
    predictions = model.predict(img, verbose=0)
    # Use np.argmax instead of deprecated predict_classes()
    classIndex = np.argmax(predictions, axis=-1)[0]
    probabilityValue = np.amax(predictions)
    preds = getClassName(classIndex)
    return preds, probabilityValue


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    # Return empty response for favicon to prevent 404 errors
    return '', 204


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Validate that a file was actually uploaded
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400

        f = request.files['file']

        # Some browsers submit an empty part without a filename
        if f.filename is None or f.filename.strip() == '':
            return jsonify({'error': 'No file selected for uploading'}), 400

        basepath = os.path.dirname(__file__)
        # Ensure uploads directory exists
        uploads_dir = os.path.join(basepath, 'uploads')
        if not os.path.exists(uploads_dir):
            os.makedirs(uploads_dir)

        # Ensure we always have a valid filename
        filename = secure_filename(f.filename)
        if filename == '':
            # Fallback filename if secure_filename removes everything
            import time
            filename = f"upload_{int(time.time())}.png"

        file_path = os.path.join(uploads_dir, filename)
        f.save(file_path)

        preds, probability = model_predict(file_path, model)
        result = {
            'prediction': preds,
            'confidence': float(probability)
        }
        return jsonify(result)
    return jsonify({'error': 'Invalid request method'}), 405


if __name__ == '__main__':
    # Get port from environment variable (for Render/Heroku) or use default
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=False)
