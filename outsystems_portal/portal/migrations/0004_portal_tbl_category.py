# Generated by Django 4.2.2 on 2023-11-15 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_alter_portal_tbl_description_alter_portal_tbl_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='portal_tbl',
            name='CATEGORY',
            field=models.CharField(default='', max_length=100),
        ),
    ]