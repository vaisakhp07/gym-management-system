from django.urls import path
from . import views

urlpatterns = [
    path("", views.member_list, name="member-list"),
    path("home/", views.home, name="home"),
    path("member/<int:pk>/", views.member_detail, name="member-detail"),
    path("member/add/", views.member_create, name="member-create"),
    path("member/<int:pk>/edit/", views.member_update, name="member-update"),
    path("member/<int:pk>/delete/", views.member_delete, name="member-delete"),
]
