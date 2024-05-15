# Generated by Django 4.2.11 on 2024-05-12 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Daystarapp', '0011_alter_babiesreg_babyname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignbaby',
            old_name='babyassign',
            new_name='baby_being_assigned_to',
        ),
        migrations.RenameField(
            model_name='assignbaby',
            old_name='sitterhere',
            new_name='sitter_name',
        ),
        migrations.RenameField(
            model_name='babiesreg',
            old_name='babygender',
            new_name='baby_gender',
        ),
        migrations.RenameField(
            model_name='babiesreg',
            old_name='periodstay',
            new_name='period_of_stay',
        ),
        migrations.RenameField(
            model_name='procuregive',
            old_name='procurebaby',
            new_name='baby_being_given_to',
        ),
        migrations.RenameField(
            model_name='procuregive',
            old_name='procureitem',
            new_name='procurement_item',
        ),
        migrations.RenameField(
            model_name='sitterreg',
            old_name='sittergender',
            new_name='sitter_gender',
        ),
        migrations.RenameField(
            model_name='timeout',
            old_name='babypick',
            new_name='baby_being_picked',
        ),
    ]