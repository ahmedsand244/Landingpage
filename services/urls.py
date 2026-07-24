from django.urls import path
from django.views.generic import RedirectView
from .views import ServicesView

app_name = 'services'

urlpatterns = [
    path('services/', ServicesView.as_view(), name='services_list'),
    path('technologies/', RedirectView.as_view(url='/services/', permanent=False), name='technologies_list'),
]
