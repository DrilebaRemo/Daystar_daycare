# Generated by Django 4.2.11 on 2024-05-11 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Daystarapp', '0007_remove_assignbaby_babyassign_assignbaby_babyassign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babiesreg',
            name='babygender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=100, null=True),
        ),
    ]