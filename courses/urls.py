from django.urls import path

from . import views

urlpatterns = [
    path('nielit', views.nielit, name='nielit'),
    path('icai', views.icai, name='icai'),
    path('short_term', views.short_term, name='short_term'),
]