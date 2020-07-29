from django.urls import path
from .views import evento_detail, evento_list


urlpatterns = [
    path('', evento_list, name="evento_list"),
    path('<slug:slug>/', evento_detail, name='evento_detail'),
]