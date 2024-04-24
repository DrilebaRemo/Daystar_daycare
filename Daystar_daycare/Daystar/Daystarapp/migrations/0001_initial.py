# Generated by Django 5.0.3 on 2024-04-20 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adminlogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminpassw', models.CharField(blank=True, max_length=100, null=True)),
                ('adminname', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdminReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminemail', models.CharField(blank=True, max_length=100, null=True)),
                ('adminpassw', models.CharField(blank=True, max_length=100, null=True)),
                ('adminname', models.CharField(blank=True, max_length=100, null=True)),
                ('adminphone', models.IntegerField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]