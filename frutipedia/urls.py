
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frutipedia.web.urls')),
    path('fruit/', include('frutipedia.fruit.urls')),
    path('profile/', include('frutipedia.profiles.urls')),
]
