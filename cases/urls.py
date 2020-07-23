from django.urls import path,include
from rest_framework import routers


from . import views

router = routers.DefaultRouter()
router.register(r'District', views.DistrictViewSet)

app_name='cases'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:did>', views.districtwise, name='districtwise'),
    path('edit/<int:did>', views.edit, name='edit'),
    path('updated/<int:did>', views.updated, name='updated'),
    path('data/', views.data, name='data'),
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

