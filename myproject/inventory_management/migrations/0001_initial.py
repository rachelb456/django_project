# Generated by Django 4.2.7 on 2023-11-22 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id_category', models.IntegerField(primary_key=True, serialize=False)),
                ('name_category', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': ' קטגוריה',
                'verbose_name_plural': 'קטגוריות',
            },
        ),
    ]
