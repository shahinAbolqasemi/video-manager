# Generated by Django 3.1.7 on 2021-03-09 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_auto_20210309_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionserviceassignment',
            name='related_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='plan.service', verbose_name='سرویس مربوطه'),
        ),
        migrations.AlterField(
            model_name='subscriptionserviceassignment',
            name='related_subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='plan.subscription', verbose_name='اشتراک مربوطه'),
        ),
    ]
