# Generated by Django 3.2.8 on 2021-12-08 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owners', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeesWorkSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_worked', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacation_start_date', models.DateField(blank=True, null=True)),
                ('vacation_end_date', models.DateField(blank=True, null=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='business_name')),
                ('labor_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owners.employeeroles', to_field='labor_code')),
            ],
        ),
    ]
