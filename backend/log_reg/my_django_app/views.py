from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("connection is successful!")
    return render(request, 'login_register.html')

def login(request):
    pass