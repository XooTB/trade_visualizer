from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tableview', views.tableview, name='tableview'),
    path('tableview/<str:tradeCode>', views.detailedView, name='detailview')
]

