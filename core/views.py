from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.
def homepage(request):
    # SELECT * FROM Product;
    product_list = Product.objects.all()
    
    context = {"products": product_list}
    
    # return HttpResponse("Hello Django!")
    return render(request, 'index.html', context)

def product_detail(request, id):
    # SELECT * FROM Product WHERE id = $id; -- где id - число с url
    product_object = Product.objects.get(id=id)
    context = {
        "product": product_object,
    }
    return render(request, 'product_detail.html', context)
