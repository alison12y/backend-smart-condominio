from django.db import models

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_rol

class Usuario(models.Model):
    nombre_completo = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    tipo = models.CharField(max_length=30)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_completo

class Vehiculo(models.Model):
    placa = models.CharField(max_length=20)
    tipo = models.CharField(max_length=30)
    descripcion = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class AreasComunes(models.Model):
    nombre_area = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    horario_disponible = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_area

class Reservas(models.Model):
    fecha_reserva = models.DateField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    estado = models.CharField(max_length=20)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    area = models.ForeignKey(AreasComunes, on_delete=models.CASCADE)

class Residencias(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Cuotas(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=30)
    estado = models.CharField(max_length=20)
    fecha_vencimiento = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Pagos(models.Model):
    fecha = models.DateField()
    metodo = models.CharField(max_length=30)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cuota = models.ForeignKey(Cuotas, on_delete=models.CASCADE)

class Mantenimientos(models.Model):
    tipo = models.CharField(max_length=30)
    descripcion = models.TextField()
    fecha_programada = models.DateField()
    estado = models.CharField(max_length=20)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    area = models.ForeignKey(AreasComunes, on_delete=models.CASCADE)

class EventosSeguridad(models.Model):
    descripcion = models.TextField()
    fecha_hora = models.DateTimeField()
    severidad = models.CharField(max_length=30)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Notificacion(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField()
    leido = models.BooleanField(default=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Conversacion(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Mensaje(models.Model):
    contenido = models.TextField()
    leido = models.BooleanField(default=False)
    fecha_hora = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    conversacion = models.ForeignKey(Conversacion, on_delete=models.CASCADE)
