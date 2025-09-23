from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny  # durante el desarrollo
from .models import AreasComunes, Conversacion, Cuotas, EventosSeguridad, Mantenimientos, Mensaje, Notificacion, Pagos, Reservas, Residencias, Usuario, Rol, Vehiculo
from .serializers import UsuarioSerializer, RolSerializer, VehiculoSerializer, AreasComunesSerializer, ReservasSerializer, ResidenciasSerializer, CuotasSerializer, PagosSerializer, MantenimientosSerializer, EventosSeguridadSerializer, NotificacionSerializer, ConversacionSerializer, MensajeSerializer
from rest_framework.permissions import IsAuthenticated

from core import serializers

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all().order_by("id")
    serializer_class = RolSerializer
    permission_classes = [AllowAny]

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ["nombre_completo", "ci", "email"]

    def get_queryset(self):
        # Para devolver siempre el rol anidado sin consultas extras
        return Usuario.objects.select_related("rol").order_by("id")

    @action(detail=True, methods=["patch"])
    def activar(self, request, pk=None):
        u = self.get_object(); u.activo = True; u.save()
        return Response(self.get_serializer(u).data)

    @action(detail=True, methods=["patch"])
    def desactivar(self, request, pk=None):
        u = self.get_object(); u.activo = False; u.save()
        return Response(self.get_serializer(u).data)
    
    

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [IsAuthenticated]

class AreasComunesViewSet(viewsets.ModelViewSet):
    queryset = AreasComunes.objects.all()
    serializer_class = AreasComunesSerializer
    permission_classes = [IsAuthenticated]

class ReservasViewSet(viewsets.ModelViewSet):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.rol.nombre_rol == 'admin':
            return Reservas.objects.all()
        return Reservas.objects.filter(usuario=user)

    def perform_create(self, serializer):
        area = self.request.data.get('area')
        inicio = self.request.data.get('fecha_inicio')
        fin = self.request.data.get('fecha_fin')

        conflicto = Reservas.objects.filter(
            area_id=area,
            fecha_inicio__lt=fin,
            fecha_fin__gt=inicio
        ).exists()

        if conflicto:
            raise serializers.ValidationError("El área ya está reservada en ese horario.")

        serializer.save(usuario=self.request.user)

class ResidenciasViewSet(viewsets.ModelViewSet):
    queryset = Residencias.objects.all()
    serializer_class = ResidenciasSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.rol.nombre_rol == 'admin':
            return Residencias.objects.all()
        return Residencias.objects.filter(usuario=user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class CuotasViewSet(viewsets.ModelViewSet):
    queryset = Cuotas.objects.all()
    serializer_class = CuotasSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.rol.nombre_rol == 'admin':
            return Cuotas.objects.all()
        return Cuotas.objects.filter(usuario=user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class PagosViewSet(viewsets.ModelViewSet):
    queryset = Pagos.objects.all()
    serializer_class = PagosSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.rol.nombre_rol == 'admin':
            return Pagos.objects.all()
        return Pagos.objects.filter(usuario=user)

    def perform_create(self, serializer):
        pago = serializer.save(usuario=self.request.user)
        cuota = pago.cuota
        if pago.monto >= cuota.monto:
            cuota.estado = 'pagado'
            cuota.save()

class MantenimientosViewSet(viewsets.ModelViewSet):
    queryset = Mantenimientos.objects.all()
    serializer_class = MantenimientosSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class EventosSeguridadViewSet(viewsets.ModelViewSet):
    queryset = EventosSeguridad.objects.all()
    serializer_class = EventosSeguridadSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notificacion.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class ConversacionViewSet(viewsets.ModelViewSet):
    queryset = Conversacion.objects.all()
    serializer_class = ConversacionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class MensajeViewSet(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        mensajes = Mensaje.objects.filter(usuario=self.request.user)
        mensajes.update(leido=True)
        return mensajes

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
