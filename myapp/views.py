from django.shortcuts import render
from .models import predict
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render,redirect
from .form import UploadFileForm
import cv2
from PIL import Image
import numpy as np
from .test import predict_test
# Create your views here.
def handle_uploaded_file(img):
    image=Image.open(img)
    image.save('uploads/img.jpg')
    # cv2.imwrite('img.jpg',img)
def predict_view(request):
    if request.method == 'POST':
        name=request.FILES['img_input']
        form = UploadFileForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            # if len(predict.objects.get(name=request.POST['name']))==1:
            #     Http404('name is exists')
            form.save()
            # height=predict.objects.get(name=request.POST['name']).img_input.height
            # width=predict.objects.get(name=request.POST['name']).img_input.width
            img=predict.objects.get(name=request.POST['name']).img_input
            handle_uploaded_file(img)
            predict.objects.get(name=request.POST['name']).delete()

            # print(height,width)
            img=cv2.imread('uploads/img.jpg')
            stri=predict_test(img)
            return render(request,'myapp/result.html',{'stri':stri})
    else:
        form = UploadFileForm()
    return render(request, 'myapp/predict.html', {'form' : form})
  
  
def success(request):
    return HttpResponse('successfully uploaded')