from django.shortcuts import render
from  apollaApp.forms import PatientForm
from apollaApp.models import Patient
from django.http import HttpResponseRedirect

def retrive_view(request):
    list_pat=Patient.objects.all()
    return render(request,'apollaApp/retrive.html',{'list_pat':list_pat})

def create_view(request):
    form=PatientForm()
    if request.method=='POST':
        form=PatientForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    return render(request,'apollaApp/create.html',{'form':form})

def delete_view(request,id):
    patient=Patient.objects.get(id=id)
    patient.delete()
    return HttpResponseRedirect('/')

def update_view(request,id):
    patient=Patient.objects.get(id=id)
    if request.method=="POST":
        form=PatientForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    return render(request,'apollaApp/update.html',{'patient':patient})
