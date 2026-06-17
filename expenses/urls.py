from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    path('', views.ExpenseListView.as_view(), name='expense_list'),
    path('add/', views.ExpenseCreateView.as_view(), name='expense_add'),
    path('delete/<int:pk>/', views.ExpenseDeleteView.as_view(), name='delete_expense'),
]