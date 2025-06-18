from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-house/', views.add_house, name='add-house'),
    path('house-success/', views.house_success, name='house-success'),  # Optional

    path("api/wells/", views.wells_geojson, name="wells_geojson"),
    
]
