from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
import os

from detect_image.utils import CelebrityImageDetector

# Create your views here.
class Home(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'detect_image/index.html')
    

class Predict(View):
    
    def save_image(self, uploaded_image):
        """Save file to the uploads folder"""
        try:
            with open(os.path.join('uploads',uploaded_image.name),'wb') as f:
                for chunk in uploaded_image.chunks():
                    f.write(chunk)
            return True
        except:
            return False
        
    def delete_image(self, file_path):
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except:
            return False

    def post(self, request, *args, **kwargs):
        try:
            if request.FILES:
                my_file = request.FILES['file']

                if my_file and self.save_image(my_file):
                    image_path = os.path.join('uploads', my_file.name)
                    celeb_image_detect = CelebrityImageDetector()

                    preprocess_image = celeb_image_detect.extract_features(image_path)
                    recommanded_img = celeb_image_detect.recommand(preprocess_image)
                    recommanded_img = '/uploads/' + recommanded_img

                    image_label = recommanded_img.split('/')[-2]

                    self.delete_image(image_path)
                    response = {}
                    response['response'] = 'success'
                    response['file_path'] = recommanded_img
                    response['image_label'] = image_label

                    return JsonResponse(response)
                return JsonResponse({'response': 'error', 'message': 'Something Went Wrong..! Please, Try Later..!'})
            else:
                return JsonResponse({'response': 'error', 'message': 'Data Not Found..! Please, Try Later..!'})
        except:
            return JsonResponse({'response': 'error', 'message': 'Something Went Wrong..! Please, Try Later..!'})