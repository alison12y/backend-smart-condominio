from rest_framework import serializers
from .models import *

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    rol = RolSerializer(read_only=True)
    class Meta:
        model = Usuario
        fields = '__all__'

class VehiculoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)

    class Meta:
        model = Vehiculo
        fields = '__all__'


class AreasComunesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreasComunes
        fields = '__all__'

class ReservasSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    area = AreasComunesSerializer(read_only=True)
    class Meta:
        model = Reservas
        fields = '__all__'

class ResidenciasSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    class Meta:
        model = Residencias
        fields = '__all__'

class CuotasSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    class Meta:
        model = Cuotas
        fields = '__all__'

class PagosSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    cuota = CuotasSerializer(read_only=True)
    class Meta:
        model = Pagos
        fields = '__all__'

class MantenimientosSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    area = AreasComunesSerializer(read_only=True)
    class Meta:
        model = Mantenimientos
        fields = '__all__'

class EventosSeguridadSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    class Meta:
        model = EventosSeguridad
        fields = '__all__'

class NotificacionSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    class Meta:
        model = Notificacion
        fields = '__all__'

class ConversacionSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    class Meta:
        model = Conversacion
        fields = '__all__'

class MensajeSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    conversacion = ConversacionSerializer(read_only=True)
    class Meta:
        model = Mensaje
        fields = '__all__'
