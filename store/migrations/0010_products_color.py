# Generated by Django 3.1.4 on 2021-03-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20210301_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='color',
            field=models.CharField(blank=True, default='Not-Specified', max_length=15, null=True),
        ),
    ]
