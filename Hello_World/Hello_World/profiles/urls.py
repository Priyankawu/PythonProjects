


from django.urls import path
from . import views

urlpatterns = [
    path('admin_console1', views.admin_console1, name="admin_console1"),
    path('<int:pk>/details1/', views.details1, name="details1"),
    path('<int:pk>/delete1/',views.delete1, name='delete1'),
    path('createProfile/', views.createProfile, name='createProfile'), #url name
    path('<int:pk>/confirmdelete/', views.confirmed, name="confirmed")
]