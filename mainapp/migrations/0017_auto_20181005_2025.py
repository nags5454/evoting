# Generated by Django 2.0.6 on 2018-10-05 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_auto_20181005_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aadhar_card',
            name='sex',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='voter_id',
            name='v_sex',
            field=models.CharField(max_length=6),
        ),
    ]
