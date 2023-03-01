
from sklearn.metrics.pairwise import cosine_similarity
from keras_vggface.utils import preprocess_input
from keras_vggface.vggface import VGGFace
from mtcnn import MTCNN

from PIL import Image
import numpy as np
import pickle
import cv2

class CelebrityImageDetector:
    
    detector = MTCNN()
    model = VGGFace(model='resnet50', include_top=False,input_shape=(224,224,3), pooling='avg')
    feature_list = pickle.load(open('detect_image\embedding.pkl','rb'))
    file_names = pickle.load(open('detect_image\\file_names.pkl','rb'))
    
    def extract_features(self, image_path):
        
        # load image and detect face from image
        test_img = cv2.imread(image_path)
        results = self.detector.detect_faces(test_img)
        x, y, width, height = results[0]['box']
        face_image = test_img[y:y+height, x:x+width]

        # Extract its features
        image = Image.fromarray(face_image)
        image = image.resize((224, 224))
        face_array = np.asarray(image)
        face_array = face_array.astype('float32')

        expanded_img = np.expand_dims(face_array,axis=0)
        preprocessed_img = preprocess_input(expanded_img)

        result = self.model.predict(preprocessed_img).flatten()

        return result

    def recommand(self, preprocessed_img):
        # find the cosine distance of preprocessed_img with all other feature
        similaries = []
        for i in range(len(self.feature_list)):
           similaries.append(cosine_similarity(preprocessed_img.reshape(1, -1), self.feature_list[i].reshape(1, -1))[0][0])

        similar_celeb = sorted(enumerate(similaries), reverse=True, key=lambda x:x[1])[0]
        file_path = self.file_names[similar_celeb[0]]

        return file_path
