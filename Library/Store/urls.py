
from django.urls import path
from . import views

app_name = 'Store'
#namespacing of url patterns avoid clashes between views inbetween 2 apps having the same name
urlpatterns = [
    path('', views.index,name='index'),
    path('<int:id>/',views.details,name='details'),
    path('add/',views.add_book,name='add_book'),
    path('<int:id>/update/',views.update_book,name='update_book'),
    path('<int:id>/delete/',views.delete_book,name='delete_book'),
]
