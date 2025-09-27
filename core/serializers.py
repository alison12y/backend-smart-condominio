from rest_framework import serializers
from .models import (
    Usuario, Rol, Vehiculo, AreasComunes, Reservas, Residencias,
    Cuotas, Pagos, Mantenimientos, EventosSeguridad,
    Notificacion, Conversacion, Mensaje
)


# =============================
# ROLES Y USUARIOS
# =============================

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ["id", "nombre_rol", "descripcion"]


class UsuarioSerializer(serializers.ModelSerializer):
    # Alias para nombre (frontend lo usa como "nombre")
    nombre = serializers.CharField(source="nombre_completo")

    # Lectura: objeto anidado del rol
    rol = RolSerializer(read_only=True)

    # Lectura: solo nombre del rol
    rol_nombre = serializers.CharField(source="rol.nombre_rol", read_only=True)

    # Escritura: id del rol
    rol_id = serializers.PrimaryKeyRelatedField(
        source="rol", queryset=Rol.objects.all(), write_only=True
    )

    class Meta:
        model = Usuario
        fields = [
            "id", "ci", "nombre", "email", "telefono", "direccion",
            "rol", "rol_id", "rol_nombre", "activo"
        ]


# =============================
# RESTO DE ENTIDADES
# =============================

class VehiculoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)

    class Meta:
        model = Vehiculo
        fields = "__all__"


class AreasComunesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreasComunes
        fields = "__all__"


class ReservasSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    area = AreasComunesSerializer(read_only=True)

    class Meta:
        model = Reservas
        fields = "__all__"


class ResidenciasSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)

    class Meta:
        model = Residencias
        fields = "__all__"


class CuotasSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)

    class Meta:
        model = Cuotas
        fields = "__all__"


class PagosSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    cuota = CuotasSerializer(read_only=True)

    class Meta:
        model = Pagos
        fields = "__all__"


class MantenimientosSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    area = AreasComunesSerializer(read_only=True)

    class Meta:
        model = Mantenimientos
        fields = "__all__"


class EventosSeguridadSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)

    class Meta:
        model = EventosSeguridad
        fields = "__all__"


class NotificacionSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)

    class Meta:
        model = Notificacion
        fields = "__all__"


class ConversacionSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)

    class Meta:
        model = Conversacion
        fields = "__all__"


class MensajeSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    conversacion = ConversacionSerializer(read_only=True)

    class Meta:
        model = Mensaje
        fields = "__all__"
