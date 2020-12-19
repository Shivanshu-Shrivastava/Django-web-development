from django.shortcuts import render

from .form import create_form,form_maping_with_model
# Create your views here.
def form_map_to_model(request):
    if request.method=="POST":
        form = form_maping_with_model(request.POST or None)
        if form.is_valid():
            form.save()
            form = form_maping_with_model()
    else:
        form = form_maping_with_model()
    context={
        "form":form

    }
    return render(request, "pages/form.html", context)

# def forms_view(request):
#
#     if request.method=="POST":
#         form = create_form(request.POST)
#         if form.is_valid():
#             form = create_form(request.POST)
#     else:
#         form=create_form()
#     context={
#         "form":form
#     }
#     return render(request,"pages/form.html",context)
def index(request):
    context={
        "lsit":[1,2,3,4],
        "open":"stayam"
    }
    return render(request,'pages/index.html',context)
def written(request):
    return render(request,'pages/written.html')
def reading(request):
    return render(request,'pages/reading.html')
def playing(request):
    return render(request,'pages/playing.html')
