# Generated by Django 4.0.3 on 2022-03-11 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='user',
        ),
        migrations.AddField(
            model_name='detail',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='detail',
            name='firstname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='detail',
            name='lastname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='detail',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
