from django.urls import path
from .views import spec_list, spec_detail

urlpatterns = [
    path('', spec_list, name='spec-list'),  
    path('<int:pk>/', spec_detail, name='spec-detail'),  
]