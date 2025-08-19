from django.contrib import admin
from django.urls import path, include  # Make sure to import include
from members.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('members/', include('members.urls')),
    path('trainers/', include('trainers.urls')),
]


