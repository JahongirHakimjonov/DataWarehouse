from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r"analytics_warehouse_data", ProductViewSet, basename="analytics_warehouse_data")

urlpatterns = router.urls
