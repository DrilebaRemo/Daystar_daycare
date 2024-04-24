# Generated by Django 5.0.3 on 2024-04-20 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Daystarapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Babiesreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('babyname', models.CharField(blank=True, max_length=100, null=True)),
                ('babyage', models.IntegerField(blank=True, default=0, null=True)),
                ('babygender', models.CharField(blank=True, max_length=100, null=True)),
                ('babyloc', models.CharField(blank=True, max_length=100, null=True)),
                ('babyparent', models.CharField(blank=True, max_length=100, null=True)),
                ('babyno', models.IntegerField(blank=True, max_length=100, null=True)),
                ('babypay', models.CharField(blank=True, default='Ugx', max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sitterreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sittername', models.CharField(blank=True, max_length=100, null=True)),
                ('siiterbirth', models.DateTimeField(blank=True, null=True)),
                ('sittergender', models.CharField(blank=True, max_length=100, null=True)),
                ('sitterloc', models.CharField(blank=True, max_length=100, null=True)),
                ('sitterNIN', models.IntegerField(blank=True, max_length=100, null=True)),
                ('sitterno', models.IntegerField(blank=True, max_length=100, null=True)),
                ('sitterkin', models.CharField(blank=True, max_length=100, null=True)),
                ('sitterreco', models.CharField(blank=True, max_length=100, null=True)),
                ('sitterreligion', models.CharField(blank=True, max_length=100, null=True)),
                ('sittereduc', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='adminreg',
            name='adminphone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]