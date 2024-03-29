# Generated by Django 3.1.7 on 2021-04-20 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('title', models.CharField(max_length=128, verbose_name='عنوان')),
                ('related_creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_creator_related', related_query_name='service_creator', to=settings.AUTH_USER_MODEL, verbose_name='ایجاد کننده')),
            ],
            options={
                'verbose_name': 'سرویس',
                'verbose_name_plural': 'سرویس ها',
            },
        ),
        migrations.CreateModel(
            name='ServiceField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('title', models.CharField(max_length=64)),
                ('related_creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='servicefield_creator_related', related_query_name='servicefield_creator', to=settings.AUTH_USER_MODEL, verbose_name='ایجاد کننده')),
            ],
            options={
                'verbose_name': 'فیلد سرویس',
                'verbose_name_plural': 'فیلدهای سرویس',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('title', models.CharField(max_length=128, verbose_name='عنوان')),
                ('related_creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscription_creator_related', related_query_name='subscription_creator', to=settings.AUTH_USER_MODEL, verbose_name='ایجاد کننده')),
            ],
            options={
                'verbose_name': 'اشتراک',
                'verbose_name_plural': 'اشتراک ها',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionServiceAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('related_creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscriptionserviceassignment_creator_related', related_query_name='subscriptionserviceassignment_creator', to=settings.AUTH_USER_MODEL, verbose_name='ایجاد کننده')),
                ('related_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='plan.service', verbose_name='سرویس مربوطه')),
                ('related_subscription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='plan.subscription', verbose_name='اشتراک مربوطه')),
            ],
            options={
                'verbose_name': 'سرویس در اشتراک',
                'verbose_name_plural': 'سرویس های اشتراک',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionServiceAssignmentField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('related_creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscriptionserviceassignmentfield_creator_related', related_query_name='subscriptionserviceassignmentfield_creator', to=settings.AUTH_USER_MODEL, verbose_name='ایجاد کننده')),
                ('related_service_field', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='plan.servicefield')),
                ('related_subscription_service_assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.subscriptionserviceassignment')),
            ],
            options={
                'verbose_name': 'فیلد متصل شده به سرویس اشتراک',
                'verbose_name_plural': 'فیلد های متصل شده به سرویس اشتراک',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('related_creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscriptionassignment_creator_related', related_query_name='subscriptionassignment_creator', to=settings.AUTH_USER_MODEL, verbose_name='ایجاد کننده')),
                ('related_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('related_subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.subscription')),
            ],
            options={
                'verbose_name': 'انتساب اشتراک',
                'verbose_name_plural': 'انتساب اشتراک ها',
            },
        ),
        migrations.CreateModel(
            name='ServiceFieldAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('related_creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='servicefieldassignment_creator_related', related_query_name='servicefieldassignment_creator', to=settings.AUTH_USER_MODEL, verbose_name='ایجاد کننده')),
                ('related_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.service')),
                ('related_service_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.servicefield')),
            ],
            options={
                'verbose_name': 'فیلد سرویس',
                'verbose_name_plural': 'فیلد های سرویس',
            },
        ),
        migrations.AddIndex(
            model_name='subscriptionserviceassignmentfield',
            index=models.Index(fields=['related_subscription_service_assignment'], name='plan_subscr_related_c92ee9_idx'),
        ),
        migrations.AddIndex(
            model_name='subscriptionserviceassignmentfield',
            index=models.Index(fields=['related_service_field'], name='plan_subscr_related_c166e8_idx'),
        ),
        migrations.AddIndex(
            model_name='subscriptionserviceassignmentfield',
            index=models.Index(fields=['related_subscription_service_assignment', 'related_service_field'], name='plan_subscr_related_059595_idx'),
        ),
        migrations.AddIndex(
            model_name='subscriptionserviceassignment',
            index=models.Index(fields=['related_subscription'], name='plan_subscr_related_47ea07_idx'),
        ),
        migrations.AddIndex(
            model_name='subscriptionserviceassignment',
            index=models.Index(fields=['related_service'], name='plan_subscr_related_1534e9_idx'),
        ),
        migrations.AddIndex(
            model_name='subscriptionserviceassignment',
            index=models.Index(fields=['related_subscription', 'related_service'], name='plan_subscr_related_c2f96f_idx'),
        ),
        migrations.AddIndex(
            model_name='subscriptionassignment',
            index=models.Index(fields=['related_subscription'], name='plan_subscr_related_e34683_idx'),
        ),
        migrations.AddIndex(
            model_name='subscriptionassignment',
            index=models.Index(fields=['related_customer'], name='plan_subscr_related_ef1925_idx'),
        ),
        migrations.AddIndex(
            model_name='subscriptionassignment',
            index=models.Index(fields=['related_subscription', 'related_customer'], name='plan_subscr_related_cbc142_idx'),
        ),
        migrations.AddIndex(
            model_name='subscription',
            index=models.Index(fields=['title'], name='plan_subscr_title_7db776_idx'),
        ),
        migrations.AddIndex(
            model_name='servicefieldassignment',
            index=models.Index(fields=['related_service'], name='plan_servic_related_bbb30d_idx'),
        ),
        migrations.AddIndex(
            model_name='servicefieldassignment',
            index=models.Index(fields=['related_service_field'], name='plan_servic_related_fee711_idx'),
        ),
        migrations.AddIndex(
            model_name='servicefieldassignment',
            index=models.Index(fields=['related_service_field', 'related_service'], name='plan_servic_related_2c7b24_idx'),
        ),
        migrations.AddIndex(
            model_name='servicefield',
            index=models.Index(fields=['title'], name='plan_servic_title_6c331f_idx'),
        ),
        migrations.AddIndex(
            model_name='service',
            index=models.Index(fields=['title'], name='plan_servic_title_616541_idx'),
        ),
    ]
