from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects
from django.http import FileResponse
from random import randint
import time
def send_file(response):

    img = open('coool/booot/images/booot/images/photo_2023-04-13_10-03-09.jpg', 'rb')

    response = FileResponse(img)

    return response

def index(request):
    image = Projects.objects.all()
    way = randint(1,4)
    match way:
        case 1:
            time.sleep(randint(1,10)) 
            response = HttpResponse(content_type="image/jpeg")
            return send_file(response)   
        case 2:
            response = HttpResponse(content_type="image/jpeg")
            return send_file(response)
        case 3:
            return render(request, 'booot/index.html', {'images' : image})
        case 4:
            return render(request, 'booot/index2.html')
    # return send_file(response)
    # return render(request, 'booot/index.html', {'images' : image})
    # return render(request, 'booot/images/booot/imagesphoto_2023-04-13_10-03-09.jpg')
# Create your views here.
