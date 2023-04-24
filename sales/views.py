from django.shortcuts import render

# Create your views here.
#This function takes the request coming from the web application and
#returns the template as a response.
def home(request):
    return render(request, "sales/home.html")
