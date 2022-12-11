

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('gallrey', include('gallrey.urls')),
    path('about', include('aboutUs.urls')),
    path('courses', include('courses.urls')),
]
