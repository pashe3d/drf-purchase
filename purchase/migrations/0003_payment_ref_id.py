# Generated by Django 3.2.5 on 2021-07-28 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_alter_payment_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='ref_id',
            field=models.TextField(null=True),
        ),
    ]
