from django.urls import path
from onlineshop.views import OrderView

urlpatterns = [
    
    path('order/', OrderView.as_view(), name='order'),
]


