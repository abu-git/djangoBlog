# Generated by Django 2.1.3 on 2018-11-27 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='signature',
            field=models.CharField(default='together we stand, divided we fall', max_length=140),
        ),
    ]
