# Generated by Django 3.2 on 2022-08-14 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='shopuser',
            name='lng',
            field=models.FloatField(null=True),
        ),
    ]
