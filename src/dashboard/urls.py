from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('page_import/', views.page_csv, name='import'),
    path('import_csv/', views.import_csv, name="import_csv"),
    path('graph1/', views.graph1,name='graph1'),
    path('graph2/', views.graph2,name='graph2'),
    path('graph3/', views.graph3,name='graph3'),
]