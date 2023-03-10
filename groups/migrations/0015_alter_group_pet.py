# Generated by Django 4.1.6 on 2023-02-21 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0002_alter_pet_sex"),
        ("groups", "0014_alter_group_pet"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="pet",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="group",
                to="pets.pet",
            ),
        ),
    ]
