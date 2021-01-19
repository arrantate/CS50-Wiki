from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<page_title>", views.detail_page, name="detail_page"),
]
