# Generated by Django 4.0.3 on 2022-04-22 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dusunen', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='slugs',
            field=models.SlugField(max_length=200, null=True),
        ),
    ]