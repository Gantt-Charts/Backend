# Generated by Django 5.0.2 on 2024-03-04 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_task_dependencies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dependencies',
            field=models.ManyToManyField(blank=True, to='api.task'),
        ),
    ]
