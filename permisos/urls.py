from rest_framework.routers import DefaultRouter
from permisos.views import PermisosViewSet

router = DefaultRouter()
router.register(r'', PermisosViewSet)

urlpatterns = router.urls

