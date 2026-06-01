from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def freshers(request):
    return render(request, 'freshers.html')

def homies(request):
    return render(request, 'homies.html')

def temple(request):
    return render(request, 'temple.html')

def phase(request):
    return render(request, 'phase.html')

def lastday(request):
    return render(request, 'lastday.html')

def quotes(request):
    return render(request, 'quotes.html')