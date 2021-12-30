from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.studentview,name='home'),
    path('add/',views.addView,name='add_stu'),
    path('delete/<int:i>/',views.delete,name='del'),
    path('update/<int:i>/',views.update,name='upd')
]