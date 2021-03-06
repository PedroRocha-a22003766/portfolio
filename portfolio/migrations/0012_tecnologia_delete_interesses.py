# Generated by Django 4.0.4 on 2022-05-29 20:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_alter_projeto_participantes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('acronimo', models.CharField(max_length=64)),
                ('anoDeCriacao', models.IntegerField(default=6, validators=[django.core.validators.MinValueValidator(limit_value=1800), django.core.validators.MaxValueValidator(limit_value=2022)])),
                ('criador', models.CharField(max_length=64)),
                ('descricao', models.CharField(max_length=512)),
            ],
        ),
        migrations.DeleteModel(
            name='Interesses',
        ),
    ]
