# Generated by Django 4.1.3 on 2022-11-30 00:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('release_date', models.DateField()),
                ('chapter', models.IntegerField()),
                ('season', models.IntegerField()),
                ('rating', models.FloatField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='serie')),
                ('director', models.CharField(max_length=40)),
                ('actor', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('studio', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ['-release_date'],
                'unique_together': {('name', 'studio')},
            },
        ),
    ]
