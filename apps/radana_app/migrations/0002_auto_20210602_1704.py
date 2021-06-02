# Generated by Django 2.2.4 on 2021-06-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radana_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='items_order',
            field=models.ManyToManyField(related_name='orders', to='radana_app.Item'),
        ),
    ]
