# Generated by Django 3.1.4 on 2021-01-10 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='logo',
            name='order',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
