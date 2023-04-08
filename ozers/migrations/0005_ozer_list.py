# Generated by Django 4.2 on 2023-04-08 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("list", "0001_initial"),
        ("ozers", "0004_totalozer"),
    ]

    operations = [
        migrations.AddField(
            model_name="ozer",
            name="list",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ozers",
                to="list.list",
            ),
            preserve_default=False,
        ),
    ]