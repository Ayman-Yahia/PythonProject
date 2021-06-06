# Generated by Django 2.2.4 on 2021-06-04 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radana_app', '0009_auto_20210604_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(related_name='items', to='radana_app.Item'),
        ),
    ]
