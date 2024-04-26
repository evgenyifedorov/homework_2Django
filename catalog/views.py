from django.shortcuts import render, get_object_or_404
from catalog.models import Product


# Create your views here.
def index(request):
    return render(request, "main/home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Ваше сообщение: {name}, {phone}, {message}")
        with open("write.txt", "wt", encoding="UTF-8") as file:
            file.write(f"Ваше сообщение: {name}, {phone}, {message}")

    return render(request, "main/contacts.html")


def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)
