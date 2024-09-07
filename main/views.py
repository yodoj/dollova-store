from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name':"Teddy bear",
        'price':'Rp100.000',
        'description':'Cute and huggable teddy bear with premium materials for ultimate coziness.'
    }

    return render(request, "main.html", context)