from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
import os

# Create your views here.
def index(request):
    image_files = ['img/대문2/향1대문.png', 'img/대문2/향5대문.png',]  # 변경 가능
    return render(request, 'index.html', {'image_files': image_files})

def block5(request):
    image_files = ['img/5블럭/5BL블럭 안내.png', 'img/5블럭/향동5대문.png', 'img/5블럭/향5개요.png', 'img/5블럭/5특징1100_800.png',]
    image_files2 = os.listdir('./static/img/5블럭/향5배치도')
    prefix = 'img/5블럭/향5배치도/'
    image_files2 = [prefix + file_name for file_name in image_files2]
    return render(request, '5block.html', {'image_files': image_files, 'image_files2': image_files2,})

def block6(request):
    image_files = ['img/6블럭/6BL블럭 안내.png', 'img/6블럭/향동6대문.png', 'img/6블럭/향6개요.png', 'img/6블럭/6특징1100_800.png',]  # 변경 가능
    image_files2 = os.listdir('./static/img/6블럭/향6배치도')
    prefix = 'img/6블럭/향6배치도/'
    image_files2 = [prefix + file_name for file_name in image_files2]
    return render(request, '6block.html', {'image_files': image_files, 'image_files2': image_files2,})

def block7(request):
    image_files = ['img/7블럭/7BL블럭 안내.png', 'img/7블럭/향동7대문.png', 'img/7블럭/향7개요.png', 'img/7블럭/7특징1100_800.png',]  # 변경 가능
    image_files2 = os.listdir('./static/img/7블럭/향7배치도')
    prefix = 'img/7블럭/향7배치도/'
    image_files2 = [prefix + file_name for file_name in image_files2]
    return render(request, '7block.html', {'image_files': image_files, 'image_files2': image_files2,})

def block8(request):
    image_files = ['img/8블럭/8BL블럭 안내.png', 'img/8블럭/향동8대문.png', 'img/8블럭/향8개요.png', 'img/8블럭/8특징1100_800.png',]  # 변경 가능
    image_files2 = os.listdir('./static/img/8블럭/향8배치도')
    prefix = 'img/8블럭/향8배치도/'
    image_files2 = [prefix + file_name for file_name in image_files2]
    return render(request, '8block.html', {'image_files': image_files, 'image_files2': image_files2,})

def block9(request):
    image_files = ['img/9블럭/9BL블럭 안내.png', 'img/9블럭/향동9대문.png', 'img/9블럭/향9개요.png', 'img/9블럭/9특징1100_800.png',]  # 변경 가능
    image_files2 = os.listdir('./static/img/9블럭/향9배치도')
    prefix = 'img/9블럭/향9배치도/'
    image_files2 = [prefix + file_name for file_name in image_files2]
    return render(request, '9block.html', {'image_files': image_files, 'image_files2': image_files2,})

def block1(request):
    image_files = ['img/1블럭/1BL블럭 안내.png', 'img/1블럭/향동1대문.png', 'img/1블럭/향1개요.png', 'img/1블럭/1특징1100_800.png',]  # 변경 가능
    image_files2 = os.listdir('./static/img/1블럭/향1배치도')
    prefix = 'img/1블럭/향1배치도/'
    image_files2 = [prefix + file_name for file_name in image_files2]
    return render(request, '1block.html', {'image_files': image_files, 'image_files2': image_files2,})

def block4(request):
    image_files = ['img/4블럭/4BL블럭 안내.png', 'img/4블럭/향동4대문.png', 'img/4블럭/향4개요.png', 'img/4블럭/4특징1100_800.png',]  # 변경 가능
    image_files2 = os.listdir('./static/img/4블럭/향4배치도')
    prefix = 'img/4블럭/향4배치도/'
    image_files2 = [prefix + file_name for file_name in image_files2]
    return render(request, '4block.html', {'image_files': image_files, 'image_files2': image_files2,})

def page_not_found(request, exception):
    return render(request, 'common/404.html', {})