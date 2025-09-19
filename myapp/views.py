from django.shortcuts import render,redirect,get_object_or_404
from . models import User

# Create your views here.
def userreg(request):
    return render(request,"register.html")


def insertuser(request):
    vuid=request.POST['pid']
    vuname=request.POST['name']
    vuemail=request.POST['email']
    vucont=request.POST['contact']

    us=User(uid=vuid,uname=vuname,uemail=vuemail, ucount=vucont)
    us.save()
    return render(request,'index.html')

def index(request):
    return render(request,"index.html")

def viewuser(request):
    user=User.objects.all()
    return render(request,"viewuser.html",{'userdata':user})


def deleteuser(request,id):
    us=User.objects.filter(uid=id)
    us.delete()
    return redirect('viewuser')


def update_user(request,uid):
    user =get_object_or_404(User,uid=uid)
    if request.method=="POST":
        user.uname=request.POST.get("name")
        user.uemail=request.POST.get("email")
        user.ucont=request.POST.get("contact")
        user.save()
        return redirect("viewuser")
    return render(request,"edit.html",{"user" :user})


def home_page(request):
    return render(request,"home.html")




