# Generated by Django 3.2 on 2022-08-19 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20220819_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='shop_logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='coupon',
            name='shop_sector',
            field=models.CharField(max_length=10, null=True),
        ),
    ]