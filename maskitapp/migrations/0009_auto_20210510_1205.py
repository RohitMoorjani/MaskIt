# Generated by Django 3.2.1 on 2021-05-10 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maskitapp', '0008_auto_20210509_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_table',
            name='image4',
            field=models.ImageField(null=True, upload_to='maskitapp/images'),
        ),
        migrations.AddField(
            model_name='employee_table',
            name='image5',
            field=models.ImageField(null=True, upload_to='maskitapp/images'),
        ),
    ]