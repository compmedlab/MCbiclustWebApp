# Generated by Django 2.0 on 2018-02-26 02:15

from django.db import migrations, models
import mcbiclustweb.models


class Migration(migrations.Migration):

    dependencies = [
        ('mcbiclustweb', '0006_auto_20180225_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='gem',
            field=models.FileField(blank=True, upload_to=mcbiclustweb.models.user_directory_path),
        ),
    ]
