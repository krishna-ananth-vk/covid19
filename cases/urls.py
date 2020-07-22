from django.urls import path

from . import views


app_name='cases'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:did>', views.districtwise, name='districtwise'),
    path('edit/<int:did>', views.edit, name='edit'),
    path('updated/<int:did>', views.updated, name='updated'),
    path('data/', views.data, name='data')
]

