# Generated by Django 5.0.7 on 2024-08-05 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_rename_image_postmodel_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='image_url',
            field=models.ImageField(default='default_blog.png', upload_to='Images'),
        ),
    ]
