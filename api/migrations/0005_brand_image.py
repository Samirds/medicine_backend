# Generated by Django 4.2 on 2023-06-11 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_product_information_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, max_length=250, null=True, upload_to='Images'),
        ),
    ]
