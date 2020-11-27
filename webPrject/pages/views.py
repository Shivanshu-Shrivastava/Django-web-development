from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pages/index.html')
def written(request):
    return render(request,'pages/written.html')
def reading(request):
    return render(request,'pages/reading.html')
def playing(request):
    return render(request,'pages/playing.html')
