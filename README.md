# Animal Classifier Web App

A web application for classifying animal images using deep learning. Recognizes three categories: cats, dogs, and snakes.

## ✨ Features
- Real-time image classification
- Confidence level visualization
- Modern intuitive interface
- Error handling and user guidance
- Cross-platform compatibility (Windows/Linux/macOS)

## ⚙️ Technology Stack
- **Backend**: Python, Flask
- **AI**: TensorFlow/Keras, MobileNetV2
- **Frontend**: HTML5, CSS3, JavaScript
- **Image Processing**: Keras Image Preprocessing

## 🚀 Quick Start

### Requirements
- Python 3.8+
- pip

### Installation
```bash
# Clone repository
git clone https://github.com/your-username/animal-classifier-web.git
cd animal-classifier-web
# Create virtual environment (recommended)
python -m venv .venv
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Linux/MacOS

# Install dependencies
pip install -r requirements.txt

Running the Application

# Start Flask development server
python app.py
```
# Access application at:
http://localhost:5000
🖼️ Using the Application
Click "Choose File" to select an image

Supported formats: JPG, JPEG, PNG, AVIF

Click "Classify Image"

View results with confidence level

Upload new images with "Try Another Image"

🧠 Model Information
Architecture: MobileNetV2 base + custom classification head

Input Size: 128x128 pixels

Classes: Cats, Dogs, Snakes

Model Formats: .h5 and .keras formats included

Model Files
text
model/
├── animal_classifier.h5
├── animal_classifier.keras
├── animal_classifier_weights.h5
└── class_names.json
📂 Project Structure
text
FlaskProject/
├── .venv/                 # Virtual environment (ignored by Git)
├── model/                 # Model files
│   ├── animal_classifier.h5
│   ├── animal_classifier.keras
│   ├── animal_classifier_weights.h5
│   └── class_names.json
├── static/                # Static assets (CSS/JS/Images) ( need to create )
├── uploaded/              # Sample test images
├── templates/             # HTML templates
│   ├── error.html
│   ├── index.html
│   └── result.html
├── .gitignore             # Git ignore file
├── app.py                 # Main application
└── requirements.txt       # Dependencies
⚠️ Known Limitations
Works best with clear animal images

Limited to cats, dogs, and snakes recognition

Performance may vary with unusual angles/images

Sample images in /uploaded are for testing only

🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create your feature branch (git checkout -b feature/your-feature)

Commit your changes (git commit -am 'Add some feature')

Push to the branch (git push origin feature/your-feature)

Open a pull request
