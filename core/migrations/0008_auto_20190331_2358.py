# Generated by Django 2.1.5 on 2019-03-31 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190331_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='sent_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='sent_time',
            field=models.TimeField(auto_now=True),
        ),
    ]
