# Generated by Django 3.0.8 on 2020-07-16 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20200716_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='courses.Course'),
        ),
    ]
