from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tableview', views.tableview, name='tableview'),
    path('tableview/<str:tradeCode>', views.detailedView, name='detailview')
]

"""
URL patterns for the main app.

- The empty path ('') maps to the index view.
- The path 'tableview' maps to the tableview view.
- The path 'tableview/<str:tradeCode>' maps to the detailedView view, where tradeCode is a string parameter.
"""
