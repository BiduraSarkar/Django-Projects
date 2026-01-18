
from django.urls import path
from . import views

app_name = 'Store'
#namespacing of url patterns avoid clashes between views inbetween 2 apps having the same name
urlpatterns = [
    path('', views.index,name='index'),
    path('<int:id>/',views.details,name='details'),
]
