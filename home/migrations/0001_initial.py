# Generated by Django 4.0.3 on 2022-03-11 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('address', models.CharField(blank=True, default='Nothing Here', max_length=100, null=True)),
                ('bhawan', models.CharField(default='Nothing Here', max_length=100)),
                ('gender', models.CharField(default='Female', max_length=50)),
                ('country', models.CharField(default='India', max_length=100)),
                ('state', models.CharField(default='Rajasthan', max_length=100)),
                ('zipcode', models.IntegerField(blank=True, null=True)),
                ('phone', models.BigIntegerField(blank=True, null=True)),
                ('branch', models.CharField(blank=True, max_length=100, null=True)),
                ('hobby', models.CharField(blank=True, max_length=100, null=True)),
                ('food', models.CharField(blank=True, max_length=100, null=True)),
                ('prefer', models.CharField(blank=True, max_length=100, null=True)),
                ('music', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
