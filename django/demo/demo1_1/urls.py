from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name='home'),
    path('handle_username/', views.handle_username, name='handle_username'),
    path('userinformation/', views.userinformation, name='userinformation'),
    path('courses/', views.courses, name='courses'),
    path('aboutus/',views.aboutus,name='aboutus')
]
