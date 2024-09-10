from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {   
        'app_name':"Dollova Store", 
        'name':"Nadira Aliya Nashwa", 
        'class':'PBP C'
        }

    return render(request, "main.html", context)