from django.shortcuts import render , HttpResponse
import random


def test_view(request):
    return HttpResponse(F"hello world {random.randint(1,100)}")

def html_view(request):
    return render(request,'main.html')