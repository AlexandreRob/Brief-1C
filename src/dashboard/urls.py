from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('import/', views.import_csv, name='import'),
    path('graph1/', views.graph1,name='graph1'),
    path('graph2/', views.graph2,name='graph2'),
    path('graph3/', views.graph3,name='graph3'),
]