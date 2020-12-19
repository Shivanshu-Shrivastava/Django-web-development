from django.shortcuts import render
from .models import Productmodel
# Create your views here.
def product_create_model(request):
    obj=Productmodel.objects.get(id=1)
    # context={
    #     'product':obj.Product_Name,
    #     'email':obj.Email,
    #     'mobile':obj.Mobile_no
    #
    # }
    context={
        "object":obj

    }

    return render(request,'product/detail.html',context)
