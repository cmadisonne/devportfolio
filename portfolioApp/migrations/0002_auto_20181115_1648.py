# Generated by Django 2.0.6 on 2018-11-15 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodal',
            name='message',
            field=models.TextField(max_length=500),
        ),
    ]
