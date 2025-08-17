from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, GlobalAveragePooling2D
import numpy as np
import os
import json
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='static')

# Шляхи до файлів моделі
MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model')
MODEL_PATH = os.path.join(MODEL_DIR, 'animal_classifier.h5')
WEIGHTS_PATH = os.path.join(MODEL_DIR, 'animal_classifier_weights.h5')
CLASS_NAMES_PATH = os.path.join(MODEL_DIR, 'class_names.json')


# Функція для створення архітектури моделі
def create_model():
    base_model = MobileNetV2(
        input_shape=(128, 128, 3),
        include_top=False,
        weights='imagenet',
        pooling='avg'
    )
    base_model.trainable = False

    model = Sequential([
        base_model,
        Dense(256, activation='relu'),
        Dropout(0.5),
        Dense(128, activation='relu'),
        Dropout(0.3),
        Dense(3, activation='softmax')  # 3 класи: cats, dogs, snakes
    ])

    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    return model


# Завантаження моделі
try:
    model = load_model(MODEL_PATH)
    print("Full model loaded successfully!")
except Exception as e:
    print(f"Error loading full model: {str(e)}")
    try:
        model = create_model()
        model.load_weights(WEIGHTS_PATH)
        print("Model weights loaded successfully!")
    except Exception as e2:
        print(f"Critical error loading model: {str(e2)}")
        model = create_model()

# Завантаження класів
try:
    with open(CLASS_NAMES_PATH, 'r') as f:
        class_names = json.load(f)
except:
    class_names = ['cats', 'dogs', 'snakes']  # Значення за замовчуванням

print(f"Class names: {class_names}")

# Папка для завантажень
UPLOAD_FOLDER = os.path.join(app.static_folder, 'uploaded')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
print(f"Upload folder: {UPLOAD_FOLDER}")


def prepare_image(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img)
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return render_template('error.html', message='No image uploaded')

    file = request.files['image']
    if file.filename == '':
        return render_template('error.html', message='No file selected')

    # Збереження файлу з безпечним іменем
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    print(f"Image saved to: {filepath}")

    try:
        # Підготовка та прогноз
        img = prepare_image(filepath)
        prediction = model.predict(img)[0]
        predicted_idx = np.argmax(prediction)
        predicted_class = class_names[predicted_idx]
        confidence = round(100 * np.max(prediction), 2)

        print(f"Prediction: {predicted_class} ({confidence}%)")

        # Фікс: Використовуємо лише forward slashes у шляху
        image_path = f"uploaded/{filename}"

        return render_template('result.html',
                               label=predicted_class,
                               confidence=confidence,
                               image_path=image_path)

    except Exception as e:
        print(f"Error: {str(e)}")
        return render_template('error.html', message=f'Error during prediction: {str(e)}')


if __name__ == '__main__':
    app.run(debug=True)