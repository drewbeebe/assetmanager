#api/urls.py
from django.urls import include, path
from django.conf.urls import include, re_path
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view


from .views import ManufacturerViewSet, HardwareViewSet, CompanyViewSet, ModelViewSet, LocationViewSet, CategoryViewSet, Status_labelViewSet, DepartmentViewSet, Information_SystemViewSet
#from . import views

router = DefaultRouter()
router.register(r'hardware', HardwareViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'status_labels', Status_labelViewSet)
router.register(r'models', ModelViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'manufacturers', ManufacturerViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'information_systems', Information_SystemViewSet)

urlpatterns = [
    # router URLs
    re_path('^', include(router.urls)),
    path('openapi', get_schema_view(
        title="Asset Manager",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
  
]