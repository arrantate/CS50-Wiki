from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<page_title>", views.detail_page, name="detail_page"),
    path("random/", views.random_page, name="random_page"),
    path("new/", views.new_entry, name="new_entry"),
    path("edit/<page_title>", views.edit_entry, name="edit_entry"),
    path("search/", views.search, name="search"),
]
