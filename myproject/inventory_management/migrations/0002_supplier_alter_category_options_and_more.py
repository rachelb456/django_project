# Generated by Django 4.2.7 on 2023-11-23 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id_supplier', models.IntegerField(primary_key=True, serialize=False)),
                ('name_supplier', models.CharField(max_length=255, verbose_name='שם ספק')),
                ('address_supplier', models.CharField(max_length=255, verbose_name='כתובת')),
                ('phone_number_supplier', models.CharField(max_length=255, verbose_name='מספר טלפון')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterField(
            model_name='category',
            name='name_category',
            field=models.CharField(max_length=255, verbose_name='קטגוריה'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id_product', models.IntegerField(primary_key=True, serialize=False)),
                ('name_product', models.CharField(max_length=255, verbose_name='שם מוצר')),
                ('description_product', models.TextField(verbose_name='תאור')),
                ('price_product', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='מחיר')),
                ('stock_product', models.PositiveIntegerField(verbose_name='מלאי')),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_management.category', verbose_name='קטגוריה')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id_order', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity_order', models.IntegerField(verbose_name='כמות')),
                ('date_order', models.DateTimeField(verbose_name='תאריך')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_management.product', verbose_name='מוצר')),
                ('id_supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_management.supplier', verbose_name='ספק')),
            ],
        ),
    ]