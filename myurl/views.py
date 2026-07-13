from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, "index.html")
    
def about (request):
    return HttpResponse("<h1>About</h1>")

def contact (request):
    return HttpResponse("<h1>Contact</h1>")