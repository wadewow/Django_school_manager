# Generated by Django 2.1.1 on 2018-10-18 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0002_auto_20180928_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='password',
            field=models.IntegerField(),
        ),
    ]