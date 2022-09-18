from django.urls import path

from .views import home, code_confirm

urlpatterns = [
    path("", home, name="home"),
    path("confirm/", code_confirm, name="confirm"),
]
