from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def index(request):
    return render(request=request, template_name='index.html')


def contact(request):
    return render(request=request, template_name='contact.html')

def job_listing(request):
    return render(request=request, template_name='job_listing.html')


def job_detail(request):
    return render(request=request, template_name='job_detail.html')

def about(request):
    return render(request=request, template_name='about.html')

def login_view(request):
    return render(request=request,template_name='login_template/index.html')

def logout_view(requeset):
    pass

def sign_up_view(request):
    return render(request=request,template_name='sign_up_template/index.html')