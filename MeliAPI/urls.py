
from django.urls import path
from MeliAPI import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('prices/', views.prices, name='Prices'),
    path('caja/', views.sales_manager, name='caja')

]
