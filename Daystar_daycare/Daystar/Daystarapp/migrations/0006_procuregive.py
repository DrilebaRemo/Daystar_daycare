# Generated by Django 4.2.11 on 2024-05-09 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Daystarapp', '0005_remove_assignbaby_babyassign_assignbaby_babyassign'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procuregive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procurequantity', models.IntegerField(blank=True, null=True)),
                ('procurebaby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Daystarapp.babiesreg')),
                ('procureitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Daystarapp.procure')),
            ],
        ),
    ]
