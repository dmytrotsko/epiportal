# Generated by Django 5.0.7 on 2025-04-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0003_alter_indicator_typical_revision_cadence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
    ]
