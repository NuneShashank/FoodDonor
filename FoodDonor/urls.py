from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home,name='homepage'),
    path("about_us/",views.about,name='about us'),
    path("register/",views.register,name='register')
]
