# Generated by Django 4.0.5 on 2022-06-13 04:13

from django.db import migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('simpleproject', '0004_alter_simpleformmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simpleformmodel',
            name='image',
            field=s3direct.fields.S3DirectField(),
        ),
    ]