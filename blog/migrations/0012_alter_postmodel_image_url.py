# Generated by Django 5.0.7 on 2024-08-05 04:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_postmodel_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='image_url',
            field=models.ImageField(default='default_blog.png', upload_to='Images', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])]),
        ),
    ]
