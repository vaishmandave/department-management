# from django.urls import path
# from .views import department_list, add_department, update_department, delete_department

# urlpatterns = [
#     path('', department_list, name='department_list'),
#     path('add/', add_department, name='add_department'),
#     path('edit/<int:dept_id>/', update_department, name='update_department'),
#     path('delete/<int:dept_id>/', delete_department, name='delete_department'),
# ]

from django.urls import path
from . import views
from django.urls import path
from .views import test_view

urlpatterns = [
    path('', views.department_dashboard, name='department_dashboard'),
    path('test/', test_view, name='test'),
    path('add/', views.add_department, name='add_department'),
    path('edit/<int:dept_id>/', views.edit_department, name='edit_department'),
    path('delete/<int:dept_id>/', views.delete_department, name='delete_department'),
]

