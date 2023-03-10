# Generated by Django 4.1.6 on 2023-02-21 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0002_alter_pet_sex"),
        ("groups", "0005_alter_group_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="pet",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="group",
                to="pets.pet",
            ),
        ),
    ]
