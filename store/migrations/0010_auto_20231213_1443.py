# Generated by Django 3.2 on 2023-12-13 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_customer_oederitem_order_product_shippingaddress'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OederItem',
            new_name='OrderItem',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
