# Generated by Django 2.2.4 on 2019-08-14 11:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0017_auto_20190812_0512'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInvite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invite_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Invite UUUID')),
                ('email', models.CharField(max_length=255, verbose_name='Email Address')),
                ('status', models.CharField(choices=[('accepted', 'Accepted'), ('pending', 'pending'), ('rejected', 'Rejected')], default='Pending', max_length=35, verbose_name='Invitation Status')),
                ('invite_date', models.DateTimeField(auto_now_add=True, verbose_name='Invitation DAte')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflow.Organization', verbose_name='Organization')),
            ],
            options={
                'ordering': ('invite_date',),
            },
        ),
    ]
