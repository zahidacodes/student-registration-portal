from django.shortcuts import render, HttpResponseRedirect
from .forms import myform
from .models import myclass
# Create your views here.
def show(request):
    if request.method == "POST":
        fm = myform(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data["name"]
            address = fm.cleaned_data["address"]
            branch = fm.cleaned_data["branch"]
            ph_number = fm.cleaned_data["ph_number"]
            obj = myclass(name = name, address = address, branch = branch, ph_number = ph_number)
            obj.save()
            return HttpResponseRedirect('/disp/')
    else:
            fm = myform()

    return render(request,"index.html",{"form":fm})

def disp(request):
    data =  myclass.objects.all()
    return render(request,"disp.html",{"data":data})
