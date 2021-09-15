from django.shortcuts import redirect,render
from .models import gadgets
from .forms import gadgetForm
from django.contrib import messages
# Create your views here.

def gadgetHome(request):
    gadget = gadgets.objects.all()
    return render(request,'Home.html',{'gadgets':gadget})

def gadgetDetails(request,g_id):
    gads = gadgets.objects.get(id=g_id)
    return render(request,'Details.html',{'items':gads})

def addGadget(request):
    if request.method =='POST':
        Pname = request.POST.get('name')
        Pyear = request.POST.get('year')
        Pimage = request.FILES['image']
        Pprice = request.POST.get('price')

        obj = gadgets(Name=Pname, Year=Pyear, Image=Pimage, Price=Pprice)
        obj.save()
        messages.info(request,message='New Gadget added in stock')
        
    return render(request,'AddGadget.html')

def updateGadget(request,g_id):
    obj = gadgets.objects.get(id=g_id)
    form = gadgetForm(request.POST or None,request.FILES,instance=obj)
   
    if form.is_valid():
        form.save()
        print('Updated')
    return render(request,'Update.html',{'form':form, 'value':obj})

def deleteGadget(request,g_id):
    if request.method == 'POST':
        obj_del = gadgets.objects.get(id=g_id)
        obj_del.delete()
        return redirect('/')
    return render(request, 'Delete.html')
