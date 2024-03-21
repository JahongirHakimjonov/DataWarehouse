from rest_framework.routers import DefaultRouter
from .views import DataWarehouse

router = DefaultRouter()
router.register(r"warehouse_data", DataWarehouse, basename="warehouse_data")

urlpatterns = router.urls
