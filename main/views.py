from django.shortcuts import render

def index (request): 
    return render(request, 'main/Modified_Files/index.html')