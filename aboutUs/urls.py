from django.urls import path

from . import views

urlpatterns = [

    path('aboutIns', views.aboutIns, name='aboutIns'),
    path('FacPro', views.FacPro, name='FacPro'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    
]