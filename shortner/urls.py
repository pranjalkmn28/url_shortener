from django.urls import path
from .views import URLCreateView, URLRedirectView, URLDetailView

urlpatterns = [
    path('', URLCreateView.as_view(), name='create_url'),
    path('<str:short_url>/', URLRedirectView.as_view(), name='redirect_url'),
    path('details/<str:short_url>/', URLDetailView.as_view(), name='url_detail'),
]