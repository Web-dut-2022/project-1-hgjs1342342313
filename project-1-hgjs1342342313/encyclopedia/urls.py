from django.urls import path
from django import template
from . import views

urlpatterns = [
    path("", views.Index, name="index"),
    path('wiki/<str:entry_name>/', views.AllPages, name="AllPages"),
    path('edit/<str:entry_name>/', views.Edit, name='edit'),
    path('Error', views.Error),
    path("search_item/", views.Search_item),
    path("create_new_page/", views.Create_new_page, name="create_new_page"),
    path("new_entry/", views.New_entry, name="new_entry")
]
