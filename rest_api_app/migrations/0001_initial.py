# Generated by Django 3.1.2 on 2020-10-16 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('price', models.DecimalField(decimal_places=5, max_digits=5)),
            ],
        ),
    ]
