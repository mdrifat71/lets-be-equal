from django.urls import path

from .views import CampaignListCreateView, CampaignPKView

urlpatterns = [
    path('campaign/', CampaignListCreateView.as_view()),
    path('campaign/<str:pk>', CampaignPKView.as_view())
]