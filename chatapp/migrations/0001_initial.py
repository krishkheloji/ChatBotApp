# Generated by Django 4.1.2 on 2022-10-12 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=255)),
                ('msg', models.CharField(max_length=255)),
            ],
        ),
    ]