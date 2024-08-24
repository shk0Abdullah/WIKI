from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.retrieve, name = "converter"),
    path("search/",views.search, name = "search"),
    path("search/wiki/<str:title>/", views.retrieve, name='search_wiki'),
    path("create/", views.create, name="create"),
    path("edit/",views.changes,name = "changes"),
    path("save/", views.save,name= "save"),
    path("random/",views.rand,name = 'rand')
]
