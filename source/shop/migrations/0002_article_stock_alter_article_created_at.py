# Generated by Django 4.2.7 on 2023-12-12 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата выполнения'),
        ),
    ]
