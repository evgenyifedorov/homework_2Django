from django.shortcuts import render


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
