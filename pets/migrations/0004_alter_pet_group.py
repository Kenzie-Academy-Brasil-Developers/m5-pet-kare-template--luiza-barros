# Generated by Django 4.1.7 on 2023-02-22 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("groups", "0016_remove_group_pet"),
        ("pets", "0003_pet_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="pets",
                to="groups.group",
            ),
        ),
    ]
