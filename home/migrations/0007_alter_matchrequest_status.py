# Generated by Django 4.0.3 on 2022-03-12 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_matchrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchrequest',
            name='status',
            field=models.CharField(default='no', max_length=100),
        ),
    ]
