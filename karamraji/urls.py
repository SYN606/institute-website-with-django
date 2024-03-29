from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('gallery', include('gallery.urls')),
    path('about', include('aboutUs.urls')),
    path('courses', include('courses.urls')),

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# for media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "home.views.handle_404"