from django.urls import path

from . import views

urlpatterns = [
    path('nielit', views.nielit, name='nielit'),
    path('icai', views.icai, name='icai'),
    path('short_term', views.short_term, name='short_term'),

    # nielit courses views

    path('olevel', views.olevel, name='olevel'),
    path('ccc', views.ccc, name='ccc'),
    path('ccc_plus', views.ccc_plus, name='ccc_plus'),
    path('adca', views.adca, name='adca'),
    path('eca', views.eca, name='eca'),
]