# Generated by Django 4.2.11 on 2024-04-15 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_alter_comment_id_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='id_parent',
            new_name='id_child',
        ),
    ]
