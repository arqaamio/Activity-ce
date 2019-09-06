# Generated by Django 2.2.4 on 2019-09-06 05:32

from django.db import migrations


def create_default_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    group_list = ['Administrator', 'Editor', 'Viewer', 'Org Admin']
    for item in group_list:
        group = Group(name=item)
        group.save()


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_default_groups)
    ]