"""
URL mappings for the user API
"""

from django.urls import path

from user import views


app_name = "user"

urlpatterns = [
    path("create/", views.CreateUSerView.as_view(), name="create"),
    path("tokem/", views.CreateTokenView.as_view(), name="token"),
    path("me/", views.ManageUserView.as_view(), name="me"),
]
