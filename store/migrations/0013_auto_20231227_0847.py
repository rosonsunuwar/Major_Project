# Generated by Django 3.2 on 2023-12-27 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_rename_name_shippingaddress_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kurtha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
    ]
