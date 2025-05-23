# Generated by Django 5.0.7 on 2025-04-17 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndicatorSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('short_name', models.CharField(blank=True, max_length=255, verbose_name='Short Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('maintainer_name', models.CharField(blank=True, max_length=255, verbose_name='Maintainer Name')),
                ('maintainer_email', models.CharField(blank=True, max_length=255, verbose_name='Maintainer Email')),
                ('organization', models.CharField(blank=True, max_length=255, verbose_name='Organization')),
                ('original_data_provider', models.CharField(blank=True, help_text='Original data provider of the Indicator Set', max_length=255, verbose_name='Original Data Provider')),
                ('epidata_endpoint', models.CharField(blank=True, help_text='Epidata endpoint for the Indicator Set', max_length=255, verbose_name='Epidata Endpoint')),
                ('language', models.CharField(blank=True, help_text='Language of the Indicator Set', max_length=255, verbose_name='Language')),
                ('version_number', models.CharField(blank=True, help_text='Version number of the Indicator Set', max_length=255, verbose_name='Version Number')),
                ('origin_datasource', models.TextField(blank=True, help_text='Origin data source of the Indicator Set', verbose_name='Origin Data Source')),
                ('data_type', models.CharField(blank=True, help_text='Type of data in the Indicator Set', max_length=255, verbose_name='Data Type')),
                ('preprocessing_description', models.TextField(blank=True, help_text='Description of preprocessing steps applied to the data', verbose_name='Preprocessing Description')),
                ('temporal_scope_start', models.CharField(blank=True, help_text='Start date of the temporal scope of the Indicator Set', max_length=255, verbose_name='Temporal Scope Start')),
                ('temporal_scope_end', models.CharField(blank=True, help_text='End date of the temporal scope of the Indicator Set', max_length=255, verbose_name='Temporal Scope End')),
                ('temporal_granularity', models.CharField(blank=True, help_text='Granularity of the temporal data in the Indicator Set', max_length=255, verbose_name='Temporal Granularity')),
                ('reporting_cadence', models.CharField(blank=True, help_text='Frequency of data reporting in the Indicator Set', max_length=255, verbose_name='Reporting Cadence')),
                ('reporting_lag', models.CharField(blank=True, help_text='Lag time between data collection and reporting', max_length=255, verbose_name='Reporting Lag')),
                ('revision_cadence', models.CharField(blank=True, help_text='Frequency of data revision in the Indicator Set', max_length=255, verbose_name='Revision Cadence')),
                ('demographic_scope', models.CharField(blank=True, help_text='Demographic scope of the Indicator Set', max_length=255, verbose_name='Demographic Scope')),
                ('demographic_granularity', models.CharField(blank=True, help_text='Granularity of the demographic data in the Indicator Set', max_length=255, verbose_name='Demographic Granularity')),
                ('censoring', models.CharField(blank=True, help_text='Censoring information of the Indicator Set', max_length=255, verbose_name='Censoring')),
                ('missingness', models.TextField(blank=True, help_text='Missingness information of the Indicator Set', verbose_name='Missingness')),
                ('dua_required', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown'), ('Sensor-dependent', 'Sensor-dependent')], help_text='Indicates if a data use agreement is required for the Indicator Set', max_length=255, verbose_name='Data Use Agreement Required')),
                ('license', models.CharField(blank=True, help_text='License information of the Indicator Set', max_length=255, verbose_name='License')),
                ('dataset_location', models.CharField(blank=True, help_text='Location of the dataset for the Indicator Set', max_length=255, verbose_name='Dataset Location')),
                ('documentation_link', models.CharField(blank=True, help_text='Link to the documentation for the Indicator Set', max_length=255, verbose_name='Documentation Link')),
                ('geographic_levels', models.ManyToManyField(blank=True, help_text='Geographies available in the Indicator Set', related_name='indicator_sets', to='base.geography', verbose_name='Available Geographies')),
                ('geographic_scope', models.ForeignKey(blank=True, help_text='Geographic scope of the Indicator Set', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='indicator_sets', to='base.geographicscope', verbose_name='Geographic Scope')),
                ('pathogens', models.ManyToManyField(blank=True, help_text='Pathogens included in the Indicator Set', related_name='indicator_sets', to='base.pathogen', verbose_name='Pathogens')),
                ('severity_pyramid_rungs', models.ManyToManyField(blank=True, help_text='Severity pyramid rungs of the Indicator Set', related_name='indicator_sets', to='base.severitypyramidrung', verbose_name='Severity Pyramid Rungs')),
            ],
            options={
                'verbose_name': 'Indicator Set',
                'verbose_name_plural': 'Indicator Sets',
                'ordering': ['name'],
                'indexes': [models.Index(fields=['name'], name='indicator_set_name_idx')],
            },
        ),
        migrations.AddConstraint(
            model_name='indicatorset',
            constraint=models.UniqueConstraint(fields=('name', 'original_data_provider'), name='unique_indicator_set_name'),
        ),
    ]
