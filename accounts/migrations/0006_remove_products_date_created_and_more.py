# Generated by Django 4.1.1 on 2022-09-21 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_orders_tags_products_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='date_created',
        ),
        migrations.AlterField(
            model_name='orders',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(max_length=200, null=True),
        ),
    ]
