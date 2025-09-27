import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from core.models import Rol

def seed_roles():
    roles = [
        ("Administrador", "Usuario administrador"),
        ("Residente", "Usuario residente"),
        ("Personal de Mantenimiento", "Usuario de soporte"),
        ("Personal de Seguridad", "Usuario seguridad"),
    ]

    for nombre, desc in roles:
        obj, created = Rol.objects.get_or_create(
            nombre_rol=nombre,
            defaults={"descripcion": desc}
        )
        if created:
            print(f"✅ Rol creado: {nombre}")
        else:
            print(f"ℹ️ Rol existente: {nombre}")

if __name__ == "__main__":
    seed_roles()
