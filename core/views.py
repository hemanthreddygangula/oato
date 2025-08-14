from django.shortcuts import render

def home(request):
    # templates/index.html is the uploaded oato.html
    return render(request, 'index.html')
