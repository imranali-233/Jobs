from django.urls import path
from .views import*
urlpatterns = [
    path('',index,name='index'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
    path('job_listing',job_listing,name='job_listing'),
    path('job_detail',job_detail,name='job_detail'),
    path('login_view',login_view,name='login_view'),
    path('sign_up_view',sign_up_view,name='sign_up_view')
    
]
