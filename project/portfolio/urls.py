from django.urls import path
from portfolio import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('projects',views.projects,name='projects'),
    path('blog',views.handleblog,name='handleblog'),
    path('internshipdetails',views.internshipdetails,name='internshipdetails'),
]