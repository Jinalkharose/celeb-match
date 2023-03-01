# CelebMatch
CelebMatch is a web application that uses computer vision and machine learning algorithms to match your facial features with those of famous celebrities. Simply upload a photo of yourself and let the algorithm do the rest! The application will analyze your facial features, such as the distance between your eyes and the shape of your nose, and compare them with a database of celebrity photos. Based on the analysis, the application will provide a celebrity name who share a similar facial structure with you.

## Installation
To install CelebMatch, follow these steps:

#### Clone the repository to your local machine.
#### Install the required dependencies using pip install -r requirements.txt.
#### Run the application using python manage.py runserver.
#### Navigate to http://localhost:8000 in your web browser to use the application.

## Usage
To use CelebMatch, follow these steps:

Upload a photo of yourself on the home page.
Click the "Predict" button to analyze your facial features and find your celebrity doppelganger.
The application will display a celebrity with name who share a similar facial structure with you.

## Technologies Used
CelebMatch was built using the following technologies:

Python
Django
OpenCV
TensorFlow
Keras

## Dataset
Link: https://www.kaggle.com/datasets/sushilyadav1998/bollywood-celeb-localized-face-dataset

Model Architecture
The VGG16 model was used for this project. The model was trained using transfer learning on the kaggle dataset.

## Results and Limitations
The CelebMatch application is able to accurately match facial features with celebrity photos, providing users with a fun and engaging experience. However, the accuracy of facial recognition technology can be limited by biases and inaccuracies, and the results may not always be completely accurate.

Future Improvements
In the future, CelebMatch could be improved by incorporating additional features, such as the ability to match based on hairstyle or facial hair. The accuracy of the model could also be improved by incorporating more data and fine-tuning the model architecture.
