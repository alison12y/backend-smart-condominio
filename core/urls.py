from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UsuarioViewSet,
    RolViewSet,
    VehiculoViewSet,
    AreasComunesViewSet,
    ReservasViewSet,
    ResidenciasViewSet,
    CuotasViewSet,
    PagosViewSet,
    MantenimientosViewSet,
    EventosSeguridadViewSet,
    NotificacionViewSet,
    ConversacionViewSet,
    MensajeViewSet
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'roles', RolViewSet)
router.register(r'vehiculos', VehiculoViewSet)
router.register(r'areas', AreasComunesViewSet)
router.register(r'reservas', ReservasViewSet)
router.register(r'residencias', ResidenciasViewSet)
router.register(r'cuotas', CuotasViewSet)
router.register(r'pagos', PagosViewSet)
router.register(r'mantenimientos', MantenimientosViewSet)
router.register(r'eventos', EventosSeguridadViewSet)
router.register(r'notificaciones', NotificacionViewSet)
router.register(r'conversaciones', ConversacionViewSet)
router.register(r'mensajes', MensajeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
