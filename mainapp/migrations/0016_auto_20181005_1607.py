# Generated by Django 2.0.6 on 2018-10-05 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20181005_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestent',
            name='c_img',
            field=models.CharField(max_length=50),
        ),
    ]
