# Generated by Django 4.0.6 on 2022-08-05 07:56

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
            name='Category',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('desc', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('desc', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Details',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.product')),
            ],
        ),
    ]
