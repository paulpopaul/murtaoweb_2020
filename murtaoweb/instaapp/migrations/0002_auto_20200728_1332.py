# Generated by Django 3.0.6 on 2020-07-28 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagram',
            name='estado',
            field=models.CharField(choices=[('Publicado', 'Publicado'), ('Borrador', 'Borrador')], default='Publicado', max_length=12),
        ),
    ]
