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

# Running the Application
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

⚠️ Known Limitations
Works best with clear animal images

Limited to cats, dogs, and snakes recognition

Performance may vary with unusual angles/images

Sample images in /uploaded are for testing only

INTRO

<img width="1913" height="864" alt="image" src="https://github.com/user-attachments/assets/3cd00621-f2d2-48bb-a1d5-c08da71335cf" />
<img width="1384" height="857" alt="image" src="https://github.com/user-attachments/assets/4eae524d-051f-4dfd-ba0d-64826b97fbde" />
<img width="1020" height="862" alt="image" src="https://github.com/user-attachments/assets/44a25d1a-eada-4284-839d-08b8d175cf72" />
<img width="1103" height="784" alt="image" src="https://github.com/user-attachments/assets/aaab28f8-b41d-4ef7-888e-f2d57e2147db" />


🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create your feature branch (git checkout -b feature/your-feature)

Commit your changes (git commit -am 'Add some feature')

Push to the branch (git push origin feature/your-feature)

Open a pull request
