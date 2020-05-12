# Generated by Django 2.2.10 on 2020-05-15 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formlibrary', '0004_auto_20200515_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='construction',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflow.SiteProfile'),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflow.SiteProfile'),
        ),
        migrations.AlterField(
            model_name='training',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflow.SiteProfile'),
        ),
    ]