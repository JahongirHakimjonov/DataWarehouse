from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r"warehouse_data", ProductViewSet, basename="warehouse_data")

urlpatterns = router.urls
