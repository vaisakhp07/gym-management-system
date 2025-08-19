from django.urls import path
from . import views

urlpatterns = [
    path("", views.trainer_list, name="trainer-list"),          # ✅ trainer list
    path("<int:pk>/", views.trainer_detail, name="trainer_detail"),  # ✅ trainer detail
]
