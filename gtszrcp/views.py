import os
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.conf import settings

def index(request):
    _path = os.path.join(settings.BASE_DIR, 'front', 'dist', 'index.html')
    return render_to_response(_path)