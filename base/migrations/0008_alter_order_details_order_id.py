# Generated by Django 4.0.6 on 2022-10-17 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_order_total_order_details_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_details',
            name='order_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='base.order'),
        ),
    ]
