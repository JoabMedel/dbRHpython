from rest_framework.routers import DefaultRouter
from empleados.views import EmpleadosViewSet

router = DefaultRouter()
router.register(r'', EmpleadosViewSet)

urlpatterns = router.urls

