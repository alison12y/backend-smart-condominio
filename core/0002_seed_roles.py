from django.db import migrations

def seed_roles(apps, schema_editor):
    Rol = apps.get_model("core", "Rol")
    for n in ["Administrador", "Residente", "Personal de Mantenimiento", "Personal de Seguridad"]:
        Rol.objects.get_or_create(nombre_rol=n, defaults={"descripcion": n})
exit()

def remove_roles(apps, schema_editor):
    Rol = apps.get_model("core", "Rol")
    Rol.objects.filter(
        nombre_rol__in=[
            "Administrador",
            "Residente",
            "Personal de Mantenimiento",
            "Personal de Seguridad",
        ]
    ).delete()

class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),  # deja aquí el nombre de tu última migración
    ]

    operations = [
        migrations.RunPython(seed_roles, remove_roles),
    ]