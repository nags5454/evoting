# Generated by Django 2.0.6 on 2018-10-04 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20181004_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestent',
            name='const_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='constituency_id', to='mainapp.constituency'),
        ),
    ]