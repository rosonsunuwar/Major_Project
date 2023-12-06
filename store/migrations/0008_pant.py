# Generated by Django 3.2 on 2023-12-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_saree'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='pant/')),
            ],
        ),
    ]
