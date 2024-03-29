# Generated by Django 4.2.4 on 2024-01-07 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('questions', models.CharField(max_length=5000, verbose_name='Savollar:')),
                ('answers', models.TextField(verbose_name='Javoblar:')),
            ],
            options={
                'verbose_name': 'Savollar_',
            },
        ),
    ]
