from django.urls import path
from .views import menu_list, menu_detail, menu_category

urlpatterns = [
    path('', menu_list, name="menu_list"),
    path('<slug:slug>/', menu_detail, name='menu_detail'),
    path('categoria/<slug:slug>/', menu_category, name='menu_category'),
]