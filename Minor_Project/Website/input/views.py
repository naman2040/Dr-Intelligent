from django.shortcuts import render
from django.http import HttpResponse
from .forms import fileupload

# Create your views here.
def input(request):
    if(request.method == 'POST'):
        form = fileupload(request.POST,request.FILES)
        file = request.FILES['file']
    else:
        form = fileupload()
        return render(request, 'input/input.html')
    




    
    



    

