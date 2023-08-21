from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse
from .forms import FileUpload
from django.contrib.auth.decorators import login_required
from .models import FileUpload as fp
from django.conf import settings

import os
import mimetypes

from pathlib import Path

# Create your views here.


BASE_DIR = Path(__file__).resolve().parent.parent
# print(os.path.join(BASE_DIR, 'UserFiles'))

@login_required(login_url='SignIn/')
def Home(request):
	print(request.META)
	Upload = FileUpload()
	if request.method == 'POST':
		FileSave = FileUpload(request.POST,request.FILES)
		print(FileSave.errors)
		#print(request.FILES)
		if FileSave.is_valid():
			FSave = FileSave.save()
			request.user.Key.add(FSave)
			print("Successfull")
		else:
			print('sequence failed')
	else:
		print('method error')
	context = {'FileUpload': Upload}
	return render(request, 'Cloud/Home.html', context)

# ------------------------------ FILES VIEW ------------------------------ #

def Files(request):
	Files = fp.objects.all()
	print(Files)
	return render(request, 'Cloud/Files.html' )

def About(request):
	return render(request, 'Cloud/About.html')
def Download(request,pk_download):
    dd = fp.objects.get(id=pk_download)
    ddpath = dd.file.path
    mime_type = mimetypes.guess_type(ddpath)
    filedata = open(ddpath, 'rb')
    response = HttpResponse(filedata, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename="+'(MgCloud) '+ dd.file.name
    return response
def Delete(request,pk_delete):
     delof = fp.objects.get(id=pk_delete)
     delof.delete()
     pt = delof.file.path
     os.remove(pt)
     return redirect('/Files')
def Open(request,pk_open):
        op = fp.objects.get(id=pk_open)
        oppt = op.file.path
        return FileResponse(open(oppt, 'rb'))
