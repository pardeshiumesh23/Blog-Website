# Generated by Django 5.0.7 on 2024-07-26 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_postmodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='image_url',
            field=models.ImageField(default='default_blog.png', upload_to='Images'),
        ),
    ]
