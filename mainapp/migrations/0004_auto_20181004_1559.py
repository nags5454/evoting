# Generated by Django 2.0.6 on 2018-10-04 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aadhar_card',
            name='v_VID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voter', to='mainapp.Voter_id'),
        ),
        migrations.AlterField(
            model_name='voter_id',
            name='c_CID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='constituency_ID', to='mainapp.constituency'),
        ),
    ]
