# Generated by Django 3.2.3 on 2021-05-16 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='DEFAULT VALUE', max_length=100)),
                ('price', models.CharField(default='DEFAULT VALUE', max_length=20)),
                ('stock', models.CharField(default='DEFAULT VALUE', max_length=100)),
                ('img', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'menus',
            },
        ),
    ]