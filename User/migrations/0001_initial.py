# Generated by Django 5.0 on 2023-12-29 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.CharField(max_length=300)),
                ('user_password', models.CharField(max_length=30)),
                ('user_phone', models.CharField(max_length=20)),
                ('user_country', models.CharField(max_length=20)),
            ],
        ),
    ]