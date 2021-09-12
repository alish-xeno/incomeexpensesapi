from django.urls import path
from .views import *


app_name = 'income'

urlpatterns = [

    
	# Admin Site URLs

    # Client Site URLs

    # Api Urls
    path('income/list/', IncomeListAPIView.as_view(), name="incomes"),
    path('income/<int:id>/', IncomeDetailAPIView.as_view(), name="income"),
    
]