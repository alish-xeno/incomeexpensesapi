from django.urls import path
from .views import *


app_name = 'expenses'

urlpatterns = [

    
	# Admin Site URLs

    # Client Site URLs

    # Api Urls
    path('expense/list/', ExpenseListAPIView.as_view(), name="expenses"),
    path('expense/<int:id>/', ExpenseDetailAPIView.as_view(), name="expense"),
    
]