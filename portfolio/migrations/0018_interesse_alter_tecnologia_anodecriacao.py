# Generated by Django 4.0.4 on 2022-05-31 20:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_post_delete_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interesse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=64)),
                ('descricao', models.CharField(blank=True, default='', max_length=512)),
                ('fotografia', models.ImageField(blank=True, upload_to='')),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='tecnologia',
            name='anoDeCriacao',
            field=models.IntegerField(default=1950, validators=[django.core.validators.MinValueValidator(limit_value=1900), django.core.validators.MaxValueValidator(limit_value=2022)]),
        ),
    ]