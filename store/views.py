from django.shortcuts import render

def store(request):
	context = {}
	return render(request, 'store/store.html', context)

def cart(request):
	context = {}
	return render(request, 'store/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)

def news(request):
    context = {}
    return render(request, 'store/news.html', context)

def about(request):
    context = {}
    return render(request, 'store/about.html', context)

def contacto(request):
    context = {}
    return render(request, 'store/contacto.html', context)
