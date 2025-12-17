# Traffic Sign Recognition Using Deep Learning

A web application for recognizing traffic signs using a Convolutional Neural Network (CNN) built with TensorFlow/Keras and Flask.

## Features

- 🚦 Recognize 43 different types of traffic signs
- 🌐 Web-based interface for easy image upload and prediction
- 📊 Displays prediction with confidence score
- 🎯 Real-time traffic sign classification

## Project Structure

```
traffic_sign_recognition-main/
├── app.py                 # Flask web application
├── main.py                # Model training script
├── test.py               # Real-time camera testing script
├── model.h5              # Trained CNN model
├── requirements.txt      # Python dependencies
├── labels.csv            # Traffic sign labels
├── Dataset/              # Training dataset (43 classes)
├── static/
│   ├── css/              # Stylesheets
│   └── js/               # JavaScript files
├── templates/            # HTML templates
│   ├── base.html
│   └── index.html
└── uploads/              # User uploaded images
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd traffic_sign_recognition-main
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure the model file exists**
   - The `model.h5` file should be present in the root directory
   - If not, you can train the model using `main.py`

## Usage

### Web Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Open your browser**
   - Navigate to `http://localhost:5001`
   - Upload a traffic sign image
   - Click "Predict!" to get the classification result

### Training the Model

To train your own model:

```bash
python main.py
```

This will:
- Load images from the `Dataset/` directory
- Preprocess and split the data
- Train a CNN model
- Save the model as `model.h5`

### Real-time Camera Testing

To test with a webcam:

```bash
python test.py
```

Press 'q' to quit the camera feed.

## Model Architecture

The CNN model consists of:
- Two Conv2D layers (60 filters, 5x5)
- MaxPooling2D layer
- Two Conv2D layers (30 filters, 3x3)
- MaxPooling2D layer
- Dropout layer (0.5)
- Dense layer (500 neurons)
- Dropout layer (0.5)
- Output layer (43 classes)

## Traffic Sign Classes

The model can recognize 43 different traffic signs including:
- Speed limits (20, 30, 50, 60, 70, 80, 100, 120 km/h)
- No passing signs
- Yield and Stop signs
- Direction indicators
- Warning signs
- And more...

## API Endpoints

### POST /predict
Upload an image file to get traffic sign prediction.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: image file

**Response:**
```json
{
  "prediction": "Speed Limit 50 km/h",
  "confidence": 0.9523
}
```

## Technologies Used

- **Backend:** Flask (Python web framework)
- **Deep Learning:** TensorFlow/Keras
- **Image Processing:** OpenCV, PIL
- **Frontend:** HTML, CSS, JavaScript, jQuery, Bootstrap
- **Data Processing:** NumPy, Pandas, scikit-learn

## Requirements

See `requirements.txt` for the complete list of dependencies:
- flask
- numpy
- opencv-python
- pillow
- tensorflow
- pandas
- scikit-learn
- matplotlib
- werkzeug

## Notes

- The model expects images to be resized to 32x32 pixels
- Images are preprocessed (grayscale, histogram equalization, normalization)
- The web application runs on port 5001 by default
- Uploaded images are saved in the `uploads/` directory

## Troubleshooting

### Model not found error
- Ensure `model.h5` exists in the root directory
- Train the model using `main.py` if needed

### Port already in use
- Change the port in `app.py`: `app.run(port=5001, debug=True)`

### Import errors
- Make sure all dependencies are installed: `pip install -r requirements.txt`

## License

This project is open source and available for educational purposes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Traffic Sign Recognition Project
