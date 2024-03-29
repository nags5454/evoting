# Generated by Django 2.0.6 on 2018-10-04 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20181004_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aadhar_card',
            name='v_VID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voter', to='mainapp.Voter_id'),
        ),
        migrations.AlterField(
            model_name='contestent',
            name='c_AID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aadhar_number', to='mainapp.Aadhar_card', unique=True),
        ),
    ]
