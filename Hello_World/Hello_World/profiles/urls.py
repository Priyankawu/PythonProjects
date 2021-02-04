


from django.urls import path
from . import views  # . is the main dir where view.py is

urlpatterns = [
    path('admin_console1', views.admin_console1, name="admin_console1"),
]