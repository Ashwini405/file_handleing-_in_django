from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import userReg

# Create your views here.
def valid_file(file):
   max_size=5*1024*1024
   if file.size > max_size:
      return False, "too large"
   
   all_types=['image/jpeg', 'image/png']
   if file.content_type not in all_types:
      return False , "Invalid"
   
   return True, "valid"




@csrf_exempt
def reg_user(req):
    if req.method == "POST":
        u_name = req.POST.get("name")
        u_mail = req.POST.get("email")
        u_mobile = req.POST.get("mobile")

        file_obj = req.FILES.get("pic") 

        if not file_obj:
            return JsonResponse({"error": "No file uploaded"}, status=400)

       
        userReg.objects.create(
            name=u_name,
            email=u_mail,
            mobile=u_mobile,
            pic=file_obj
        )

        return JsonResponse({"message": "User registered successfully"})

    
    return JsonResponse({"message": "Please use POST method with a file"})


