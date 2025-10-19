from django.http import HttpResponse, Http404
from django.shortcuts import render
from datetime import datetime
import os


# Create your views here.
def index(request):
    return render(request, "hellowapp/index.html")

# The texts are much longer in reality, but have
# been shortened here to save space
texts = ["Text 1", "Text 2", "Text 3"]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")
        