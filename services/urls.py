from django.urls import path
from .views import ServicesView, TechnologiesView

app_name = 'services'

urlpatterns = [
    path('services/', ServicesView.as_view(), name='services_list'),
    path('technologies/', TechnologiesView.as_view(), name='technologies_list'),
]
