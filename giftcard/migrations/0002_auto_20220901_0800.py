# Generated by Django 3.2 on 2022-09-01 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftcard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='transaction_created_at',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='transaction_updated_at',
        ),
        migrations.AlterField(
            model_name='card',
            name='balance',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
    ]