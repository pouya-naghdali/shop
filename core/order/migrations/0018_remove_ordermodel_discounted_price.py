# Generated by Django 4.2.6 on 2024-01-20 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0017_ordermodel_discounted_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='discounted_price',
        ),
    ]
