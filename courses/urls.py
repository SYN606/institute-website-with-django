from django.urls import path

from . import views

urlpatterns = [
    path('nielit', views.nielit, name='nielit'),
    path('icai', views.icai, name='icai'),
    path('short_term', views.short_term, name='short_term'),

    # nielit courses routes

    path('olevel', views.olevel, name='olevel'),
    path('ccc', views.ccc, name='ccc'),
    path('ccc_plus', views.ccc_plus, name='ccc_plus'),
    path('adca', views.adca, name='adca'),
    path('eca', views.eca, name='eca'),

    # icai courses routes

    path('cat', views.cat, name='cat'),
    path('tally', views.tally, name='tally'),

    # short-term courses routes

    path('clang', views.c_lang, name='clang'),
    path('cpp', views.cpp, name='cpp'),
    path('dca', views.dca, name='dca'),
    path('webdev', views.webdev, name='webdev'),
    path('typing', views.typing, name='typing'),
]