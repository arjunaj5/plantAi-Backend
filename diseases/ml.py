from keras.models import load_model
from keras.preprocessing import image
import numpy as np


def detect_disease(path):
    Detection = load_model('diseases/Plant_Disease_Detection.h5')
    classes = {  'Apple___Apple_scab': 0,
                 'Apple___Black_rot': 1,
                 'Apple___Cedar_apple_rust': 2,
                 'Apple___healthy': 3,
                 'Blueberry___healthy': 4,
                 'Cherry_(including_sour)___Powdery_mildew': 5,
                 'Cherry_(including_sour)___healthy': 6,
                 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': 7,
                 'Corn_(maize)___Common_rust_': 8,
                 'Corn_(maize)___Northern_Leaf_Blight': 9,
                 'Corn_(maize)___healthy': 10,
                 'Grape___Black_rot': 11,
                 'Grape___Esca_(Black_Measles)': 12,
                 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': 13,
                 'Grape___healthy': 14,
                 'Orange___Haunglongbing_(Citrus_greening)': 15,
                 'Peach___Bacterial_spot': 16,
                 'Peach___healthy': 17,
                 'Pepper__bell___Bacterial_spot': 18,
                 'Pepper__bell___healthy': 19,
                 'Potato___Early_blight': 20,
                 'Potato___Late_blight': 21,
                 'Potato___healthy': 22,
                 'Raspberry___healthy': 23,
                 'Soybean___healthy': 24,
                 'Squash___Powdery_mildew': 25,
                 'Strawberry___Leaf_scorch': 26,
                 'Strawberry___healthy': 27,
                 'Tomato_Bacterial_spot': 28,
                 'Tomato_Early_blight': 29,
                 'Tomato_Late_blight': 30,
                 'Tomato_Leaf_Mold': 31,
                 'Tomato_Septoria_leaf_spot': 32,
                 'Tomato_Spider_mites_Two_spotted_spider_mite': 33,
                 'Tomato__Target_Spot': 34,
                 'Tomato__Tomato_YellowLeaf__Curl_Virus': 35,
                 'Tomato__Tomato_mosaic_virus': 36,
                 'Tomato_healthy': 37}
    test_img = image.load_img(path,
                              target_size=(128, 128))
    test_img = image.img_to_array(test_img)
    test_img = np.expand_dims(test_img, axis=0)
    result = Detection.predict(test_img)
    a = result.argmax()
    output = a
    return output
