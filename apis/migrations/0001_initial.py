# Generated by Django 4.2 on 2023-05-09 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='anonymous', max_length=20)),
                ('age', models.IntegerField(null=True)),
                ('title', models.TextField()),
                ('context', models.TextField(max_length=255)),
            ],
        ),
    ]
