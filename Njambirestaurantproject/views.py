from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def sip(request):
    return render(request,'sample-inner-page.html')

