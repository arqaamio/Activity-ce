# Generated by Django 2.2.10 on 2020-04-03 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0011_auto_20200321_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalprojectagreement',
            name='beneficiary_type',
        ),
        migrations.RemoveField(
            model_name='historicalprojectagreement',
            name='estimated_num_direct_beneficiaries',
        ),
        migrations.RemoveField(
            model_name='historicalprojectagreement',
            name='estimated_num_indirect_beneficiaries',
        ),
        migrations.RemoveField(
            model_name='historicalprojectcomplete',
            name='beneficiary_type',
        ),
        migrations.RemoveField(
            model_name='historicalprojectcomplete',
            name='direct_beneficiaries',
        ),
        migrations.RemoveField(
            model_name='historicalprojectcomplete',
            name='indirect_beneficiaries',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='beneficiary_label',
        ),
        migrations.RemoveField(
            model_name='projectagreement',
            name='beneficiary_type',
        ),
        migrations.RemoveField(
            model_name='projectagreement',
            name='estimated_num_direct_beneficiaries',
        ),
        migrations.RemoveField(
            model_name='projectagreement',
            name='estimated_num_indirect_beneficiaries',
        ),
        migrations.RemoveField(
            model_name='projectcomplete',
            name='beneficiary_type',
        ),
        migrations.RemoveField(
            model_name='projectcomplete',
            name='direct_beneficiaries',
        ),
        migrations.RemoveField(
            model_name='projectcomplete',
            name='indirect_beneficiaries',
        ),
        migrations.AddField(
            model_name='historicalprojectagreement',
            name='estimated_num_direct_individuals',
            field=models.CharField(blank=True, help_text="Please provide achievable estimates as we will use these as our 'Targets'", max_length=255, null=True, verbose_name='Estimated number of direct individuals'),
        ),
        migrations.AddField(
            model_name='historicalprojectagreement',
            name='estimated_num_indirect_individuals',
            field=models.CharField(blank=True, help_text='This is a calculation - multiply direct individuals by average household size', max_length=255, null=True, verbose_name='Estimated Number of indirect individuals'),
        ),
        migrations.AddField(
            model_name='historicalprojectagreement',
            name='individual_type',
            field=models.CharField(blank=True, help_text='i.e. Farmer, Association, Student, Govt, etc.', max_length=255, null=True, verbose_name='Type of direct individuals'),
        ),
        migrations.AddField(
            model_name='historicalprojectcomplete',
            name='direct_individuals',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Actual Direct Individuals'),
        ),
        migrations.AddField(
            model_name='historicalprojectcomplete',
            name='indirect_individuals',
            field=models.CharField(blank=True, help_text='This is a calculation - multiply direct individuals by average household size', max_length=255, null=True, verbose_name='Estimated Number of indirect individuals'),
        ),
        migrations.AddField(
            model_name='historicalprojectcomplete',
            name='individual_type',
            field=models.CharField(blank=True, help_text='i.e. Farmer, Association, Student, Govt, etc.', max_length=255, null=True, verbose_name='Type of direct individuals'),
        ),
        migrations.AddField(
            model_name='organization',
            name='individual_label',
            field=models.CharField(default='Individuals', max_length=255, verbose_name='Individual Organization label'),
        ),
        migrations.AddField(
            model_name='projectagreement',
            name='estimated_num_direct_individuals',
            field=models.CharField(blank=True, help_text="Please provide achievable estimates as we will use these as our 'Targets'", max_length=255, null=True, verbose_name='Estimated number of direct individuals'),
        ),
        migrations.AddField(
            model_name='projectagreement',
            name='estimated_num_indirect_individuals',
            field=models.CharField(blank=True, help_text='This is a calculation - multiply direct individuals by average household size', max_length=255, null=True, verbose_name='Estimated Number of indirect individuals'),
        ),
        migrations.AddField(
            model_name='projectagreement',
            name='individual_type',
            field=models.CharField(blank=True, help_text='i.e. Farmer, Association, Student, Govt, etc.', max_length=255, null=True, verbose_name='Type of direct individuals'),
        ),
        migrations.AddField(
            model_name='projectcomplete',
            name='direct_individuals',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Actual Direct Individuals'),
        ),
        migrations.AddField(
            model_name='projectcomplete',
            name='indirect_individuals',
            field=models.CharField(blank=True, help_text='This is a calculation - multiply direct individuals by average household size', max_length=255, null=True, verbose_name='Estimated Number of indirect individuals'),
        ),
        migrations.AddField(
            model_name='projectcomplete',
            name='individual_type',
            field=models.CharField(blank=True, help_text='i.e. Farmer, Association, Student, Govt, etc.', max_length=255, null=True, verbose_name='Type of direct individuals'),
        ),
    ]