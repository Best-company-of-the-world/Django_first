import os
from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects
from django.http import FileResponse
from random import randint
import time
import os

def send_file(response):


    print(os.getcwd())
    img = open('coool/booot/images/booot/images/photo_2023-04-13_10-03-09.jpg', 'rb')

    response = FileResponse(img)

    return response

def index(request):
    image = Projects.objects.all()
    way = randint(1,4)
    if way == 1:
        time.sleep(randint(1,10))
        response = HttpResponse(content_type="image/jpeg")
        return send_file(response)
    elif way == 2:
        response = HttpResponse(content_type="image/jpeg")
        return send_file(response)
    elif way == 3:
        return render(request, 'booot/index.html', {'images' : image})
    elif way == 4:
        return render(request, 'booot/index2.html')
# Create your views here.
