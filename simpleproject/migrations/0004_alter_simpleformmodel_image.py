# Generated by Django 4.0.5 on 2022-06-13 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleproject', '0003_alter_simpleformmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simpleformmodel',
            name='image',
            field=models.ImageField(upload_to='Images/'),
        ),
    ]