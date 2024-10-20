# Generated by Django 5.1.1 on 2024-10-10 12:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscriber_name', models.CharField(max_length=100, verbose_name='نام مشتری')),
                ('subscription_cost', models.CharField(default='', max_length=100, verbose_name='قیمت اشتراک')),
                ('paypal_subscription_id', models.CharField(max_length=300, verbose_name='آیدی پی پال')),
                ('premium_subscription', models.BooleanField(default=False, verbose_name='اشتراک ویژه')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر در سایت')),
            ],
            options={
                'verbose_name': ('اشتراک',),
                'verbose_name_plural': 'اشتراک ها',
            },
        ),
    ]
