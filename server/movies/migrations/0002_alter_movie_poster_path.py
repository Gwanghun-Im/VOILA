# Generated by Django 3.2.2 on 2021-05-21 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster_path',
            field=models.TextField(blank=True, null=True),
        ),
    ]