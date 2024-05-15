# Generated by Django 4.2.11 on 2024-05-05 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Daystarapp', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignbaby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.CharField(blank=True, max_length=10, null=True)),
                ('daypay', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='dollstall',
            old_name='barbiedolls',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='dollstall',
            old_name='teddybears',
            new_name='unitprice',
        ),
        migrations.RenameField(
            model_name='procure',
            old_name='diapers',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='sales',
            old_name='amount',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='procure',
            name='fruits',
        ),
        migrations.RemoveField(
            model_name='procure',
            name='milk',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='type',
        ),
        migrations.AddField(
            model_name='babiesreg',
            name='babypay',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='babiesreg',
            name='dropper',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='babiesreg',
            name='periodstay',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='babiesreg',
            name='timein',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dollstall',
            name='dolls',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='procure',
            name='pitems',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='sell_to',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Daystarapp.babiesreg'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='timeout',
            name='babypick',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Daystarapp.babiesreg'),
        ),
        migrations.DeleteModel(
            name='Timein',
        ),
        migrations.AddField(
            model_name='assignbaby',
            name='babyassign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Daystarapp.babiesreg'),
        ),
        migrations.AddField(
            model_name='assignbaby',
            name='sitterhere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Daystarapp.sitterreg'),
        ),
    ]