from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, WarehouseViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
# router.register(r'warehouses', WarehouseViewSet, basename='warehouse')

urlpatterns = router.urls
