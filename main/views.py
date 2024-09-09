from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'product': [{
        'name':"Teddy bear",
        'price':'Rp100.000',
        'description':'Cute and huggable teddy bear with premium materials for ultimate coziness☕.',
        'stock': "30",
        'discount': "20%"},

        {'name':"Barbie doll",
        'price':'Rp200.000',
        'description':'Unleash your inner queen and slay with our gorgeous Barbie collection💅.',
        'stock': "10",
        'discount': "25%"},

        {'name':"BT21 crochet doll",
        'price':'Rp50.000',
        'description':'The adorable and cheerful BT21 crochet doll crafted with love using soft yarn🌻.',
        'stock': "35",
        'discount': "No discount"},

        ]
    }

    return render(request, "main.html", context)