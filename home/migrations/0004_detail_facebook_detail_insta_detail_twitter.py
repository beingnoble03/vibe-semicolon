# Generated by Django 4.0.3 on 2022-03-12 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_prefer_detail_hangout'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='facebook',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='detail',
            name='insta',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='detail',
            name='twitter',
            field=models.TextField(blank=True, null=True),
        ),
    ]