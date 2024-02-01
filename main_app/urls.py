from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

# djangoframework
from rest_framework import routers
from .views import EmployeeViewSet, EmployeeUpdateView

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)


urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('', include(router.urls)),
    path('api/employee/<int:pk>/', EmployeeUpdateView.as_view(), name='employee-update')
]