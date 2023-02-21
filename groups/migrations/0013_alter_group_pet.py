# Generated by Django 4.1.6 on 2023-02-21 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0002_alter_pet_sex"),
        ("groups", "0012_rename_pets_group_pet"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="pet",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="group",
                to="pets.pet",
            ),
        ),
    ]