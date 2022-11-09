from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.generic import View
from django.http.response import HttpResponse
import mimetypes
import os

class UploadView(View):

    def get(self,request,*args,**kwargs):
        return render(request,"file.html")
    def post(self,request,*args,**kwargs):
        if request.method == "POST":
            
             request_file = request.FILES['document'] if 'document' in request.FILES else None
             if request_file:
                 fs = FileSystemStorage()
                 file = fs.save(request_file.name, request_file)
                 fileurl = fs.url(file)
    
     
        return render(request, "index.html")

        

class DownloadView(View):
    # def get(self,request,*args,**kwargs):
    #     return render(request,"download.html")
    
    def get(self,request,*args,**kwargs):
        BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(BASE_DIR)
        filename = input("enter the filename u need to download")
        filepath = BASE_DIR + '/media/' + filename
        path = open(filepath, 'r')
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response


