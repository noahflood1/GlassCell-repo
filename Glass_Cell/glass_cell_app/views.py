from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "glass_cell_app/index.html")
def create_signal(request):
    return render(request,"glass_cell_app/add-distress.html")
