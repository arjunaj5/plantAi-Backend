from keras.models import load_model
from keras.preprocessing import image
import numpy as np


def detect_disease(path="../media/uploads/temp.jpeg"):
    Detection = load_model('diseases/Plant_Disease_Detection.h5')
    classes = {'Pepper__bell___Bacterial_spot': 0,
               'Pepper__bell___healthy': 1,
               'Potato___Early_blight': 2,
               'Potato___Late_blight': 3,
               'Potato___healthy': 4,
               'Tomato_Bacterial_spot': 5,
               'Tomato_Early_blight': 6,
               'Tomato_Late_blight': 7,
               'Tomato_Leaf_Mold': 8,
               'Tomato_Septoria_leaf_spot': 9,
               'Tomato_Spider_mites_Two_spotted_spider_mite': 10,
               'Tomato__Target_Spot': 11,
               'Tomato__Tomato_YellowLeaf__Curl_Virus': 12,
               'Tomato__Tomato_mosaic_virus': 13,
               'Tomato_healthy': 14}
    test_img = image.load_img(path,
                              target_size=(48, 48))
    test_img = image.img_to_array(test_img)
    test_img = np.expand_dims(test_img, axis=0)
    result = Detection.predict(test_img)
    a = result.argmax()
    # print('a:',a)
    classes = classes
    # print(classes)
    # print(len(classes))
    category = []
    for i in classes:
        category.append(i)
    for i in range(len(classes)):
        if (i == a):
            output = category[i]
    return output