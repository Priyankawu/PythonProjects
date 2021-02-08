from django.urls import path
from .import views

urlpatterns = [
    # path('what appears on web address', 'views.function to call', "{% url 'index/create etd' %}")
    path('', views.home, name='index'),
    path('create/', views.create_account, name='create'),
    path('<int:pk>/balance/', views.balance, name='balance'),
    path('transaction/', views.transaction, name='transaction')
]