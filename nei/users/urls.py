from django.urls import path

from .views import (
    list_users,
    new_user,
    edit_user,
    delete_user,
)

urlpatterns = [
    path("", list_users),
    path("edit/<str:email>", edit_user, name='edit'),
    path("newuser/", new_user),
    path("delete/<str:email>", delete_user, name='delete'),
]
