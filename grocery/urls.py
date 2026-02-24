from django.urls import path
from . import views

app_name = 'grocery'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_item, name='add'),
    path('delete/<int:item_id>/', views.delete_item, name='delete'),
    path('toggle/<int:item_id>/', views.toggle_item, name='toggle'),
    path('edit/<int:item_id>/', views.edit_item, name='edit'),
]
