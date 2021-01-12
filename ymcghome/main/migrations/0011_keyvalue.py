# Generated by Django 3.1.4 on 2021-01-10 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210110_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=300)),
                ('order', models.IntegerField(default=0, unique=True)),
            ],
        ),
    ]
