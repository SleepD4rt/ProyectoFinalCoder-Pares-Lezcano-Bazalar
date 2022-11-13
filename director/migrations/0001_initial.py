# Generated by Django 4.1.3 on 2022-11-08 18:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('awards', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('birth', models.DateField()),
                ('films', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]