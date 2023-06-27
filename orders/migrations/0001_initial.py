# Generated by Django 4.2.2 on 2023-06-27 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('status', models.CharField(max_length=2)),
                ('timestamp', models.DateTimeField()),
                ('products', models.ManyToManyField(to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField()),
                ('cafe_space_position', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.order')),
            ],
        ),
    ]
