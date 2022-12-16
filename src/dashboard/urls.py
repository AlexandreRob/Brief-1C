from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('page_csv/', views.page_csv, name='import'),
    path('graph1/', views.topG1,name='graph1'),
    path('graph1flop/', views.flopG1,name='graph1flop'),
    path('graph2/', views.topG2,name='graph2'),
    path('graph2no/', views.G2no, name='g2no'),
    path('graph2flop/', views.flopG2,name='graph2flop'),
    path('graph3/', views.graph3,name='graph3'),
    path('test/', views.test,name='test'),
]