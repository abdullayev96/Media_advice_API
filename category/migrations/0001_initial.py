# Generated by Django 4.2.4 on 2023-12-28 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Kategoriya nomi:')),
                ('body', models.CharField(max_length=200, verbose_name='Kategoriya yozuvi:')),
                ('image', models.ImageField(upload_to='note/')),
            ],
            options={
                'verbose_name': 'Kategoriya_',
            },
        ),
    ]
