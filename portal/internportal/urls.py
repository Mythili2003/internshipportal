from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('internship/',views.internship,name='internship'),
    path('login/',views.login, name='login'),
    path('display/<int:internship_id>/', views.display_details, name='display_details'),
    path('faq/',views.faqs,name='faq'), 
    path('about/',views.abouts,name='about'),
    path('contact/',views.contact,name='contact'),
    path('success/',views.success,name='success'),
    path('dscur/',views.datascience,name='datascience'),
    path('escur/',views.embedded,name='embedded'),
    path('projects/',views.projects,name='projects'),

    

   
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
