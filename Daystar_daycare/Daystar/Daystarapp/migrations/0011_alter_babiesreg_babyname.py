# Generated by Django 4.2.11 on 2024-05-11 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Daystarapp', '0010_alter_babiesreg_babyname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babiesreg',
            name='babyname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
