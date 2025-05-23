# Generated by Django 5.0.7 on 2025-04-17 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        ('datasources', '0001_initial'),
        ('indicatorsets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormatType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('display_name', models.CharField(blank=True, max_length=255, verbose_name='Display Name')),
            ],
            options={
                'verbose_name': 'Format Type',
                'verbose_name_plural': 'Format Types',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('display_name', models.CharField(blank=True, max_length=255, verbose_name='Display Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('short_description', models.TextField(blank=True, verbose_name='Short Description')),
                ('member_name', models.CharField(blank=True, max_length=255, verbose_name='Member Name')),
                ('member_short_name', models.CharField(blank=True, max_length=255, verbose_name='Member Short Name')),
                ('member_description', models.TextField(blank=True, verbose_name='Member Description')),
                ('active', models.BooleanField(default=True, help_text='Indicates if the indicator is active', verbose_name='Active')),
                ('time_type', models.CharField(blank=True, help_text='Time type of the indicator', max_length=255, verbose_name='Time Type')),
                ('time_label', models.CharField(blank=True, help_text='Label for the time type of the indicator', max_length=255, verbose_name='Time Label')),
                ('reporting_cadence', models.CharField(blank=True, help_text='Reporting cadence of the indicator', max_length=255, verbose_name='Reporting Cadence')),
                ('typical_reporting_lag', models.CharField(blank=True, help_text='Typical reporting lag of the indicator', max_length=255, verbose_name='Typical Reporting Lag')),
                ('typical_revision_cadence', models.TextField(blank=True, help_text='Typical revision cadence of the indicator', verbose_name='Typical Revision Cadence')),
                ('demographic_scope', models.CharField(blank=True, help_text='Demographic scope of the indicator', max_length=255, verbose_name='Demographic Scope')),
                ('dua_link', models.CharField(blank=True, help_text='Link to the Data Use Agreement (DUA)', max_length=255, verbose_name='DUA Link')),
                ('documentation_link', models.TextField(blank=True, help_text='Link to the documentation of the indicator', verbose_name='Documentation Link')),
                ('temporal_scope_start', models.CharField(blank=True, help_text='Start date of the temporal scope of the indicator', max_length=255, verbose_name='Temporal Scope Start')),
                ('temporal_scope_start_note', models.TextField(blank=True, help_text='Note about the temporal scope start date', verbose_name='Temporal Scope Start Note')),
                ('temporal_scope_end', models.CharField(blank=True, help_text='End date of the temporal scope of the indicator', max_length=255, verbose_name='Temporal Scope End')),
                ('temporal_scope_end_note', models.TextField(blank=True, help_text='Note about the temporal scope end date', verbose_name='Temporal Scope End Note')),
                ('is_smoothed', models.BooleanField(default=False, help_text='Indicates if the indicator is smoothed', verbose_name='Is Smoothed')),
                ('is_weighted', models.BooleanField(default=False, help_text='Indicates if the indicator is weighted', verbose_name='Is Weighted')),
                ('is_cumulative', models.BooleanField(default=False, help_text='Indicates if the indicator is cumulative', verbose_name='Is Cumulative')),
                ('has_stderr', models.BooleanField(default=False, help_text='Indicates if the indicator has standard error', verbose_name='Has Standard Error')),
                ('has_sample_size', models.BooleanField(default=False, help_text='Indicates if the indicator has sample size', verbose_name='Has Sample Size')),
                ('high_values_are', models.CharField(blank=True, help_text='Indicates if high values are good or bad', max_length=255, verbose_name='High Values Are')),
                ('data_censoring', models.TextField(blank=True, help_text='Description of data censoring applied to the indicator', verbose_name='Data Censoring')),
                ('missingness', models.TextField(blank=True, help_text='Description of missingness in the indicator', verbose_name='Missingness')),
                ('organization_access_list', models.CharField(blank=True, help_text='List of organizations that have access to the indicator', max_length=255, verbose_name='Organization Access List')),
                ('organization_sharing_list', models.CharField(blank=True, help_text='List of organizations that share the indicator', max_length=255, verbose_name='Organization Sharing List')),
                ('license', models.CharField(blank=True, help_text='License of the indicator', max_length=255, verbose_name='License')),
                ('restrictions', models.TextField(blank=True, help_text='Restrictions on the use of the indicator', verbose_name='Restrictions')),
                ('last_updated', models.DateField(blank=True, help_text='Date when the indicator was last updated', null=True, verbose_name='Last Updated')),
                ('from_date', models.DateField(blank=True, help_text='Date when the indicator was created', null=True, verbose_name='From Date')),
                ('to_date', models.DateField(blank=True, help_text='Date when the indicator was deleted', null=True, verbose_name='To Date')),
                ('indicator_availability_days', models.IntegerField(blank=True, help_text='Number of days the indicator is available', null=True, verbose_name='Indicator Availability Days')),
            ],
            options={
                'verbose_name': 'Indicator',
                'verbose_name_plural': 'Indicators',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='IndicatorGeography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aggregated_by_delphi', models.BooleanField(default=False, help_text='Indicates if the geography is aggregated by Delphi', verbose_name='Aggregated by Delphi')),
            ],
            options={
                'verbose_name': 'Indicator Geography',
                'verbose_name_plural': 'Indicator Geographies',
                'ordering': ['geography'],
            },
        ),
        migrations.CreateModel(
            name='IndicatorType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('display_name', models.CharField(blank=True, max_length=255, verbose_name='Display Name')),
            ],
            options={
                'verbose_name': 'Indicator Type',
                'verbose_name_plural': 'Indicator Types',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('display_name', models.CharField(blank=True, max_length=255, verbose_name='Display Name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
                'indexes': [models.Index(fields=['name'], name='category_name_idx')],
            },
        ),
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_category_name'),
        ),
        migrations.AddIndex(
            model_name='formattype',
            index=models.Index(fields=['name'], name='format_type_name_idx'),
        ),
        migrations.AddConstraint(
            model_name='formattype',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_format_type_name'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='available_geographies',
            field=models.ManyToManyField(blank=True, related_name='indicators', to='base.geography', verbose_name='Available Geographies'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='base',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='base_for', to='indicators.indicator', verbose_name='Base Indicator'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='indicators', to='indicators.category', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='format_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='indicators', to='indicators.formattype', verbose_name='Format Type'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='geographic_scope',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='indicators', to='base.geographicscope', verbose_name='Geographic Scope'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='indicator_set',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='indicators', to='indicatorsets.indicatorset', verbose_name='Indicator Set'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='pathogens',
            field=models.ManyToManyField(blank=True, related_name='indicators', to='base.pathogen', verbose_name='Pathogens'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='severity_pyramid_rungs',
            field=models.ManyToManyField(blank=True, related_name='indicators', to='base.severitypyramidrung', verbose_name='Severity Pyramid Rungs'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='indicators', to='datasources.sourcesubdivision', verbose_name='Source Subdivision'),
        ),
        migrations.CreateModel(
            name='OtherEndpointIndicator',
            fields=[
            ],
            options={
                'verbose_name': 'Other Endpoint Indicator',
                'verbose_name_plural': 'Other Endpoint Indicators',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('indicators.indicator',),
        ),
        migrations.AddField(
            model_name='indicatorgeography',
            name='geography',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indicator_geographies', to='base.geography', verbose_name='Geography'),
        ),
        migrations.AddField(
            model_name='indicatorgeography',
            name='indicator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indicator_geographies', to='indicators.indicator', verbose_name='Indicator'),
        ),
        migrations.AddIndex(
            model_name='indicatortype',
            index=models.Index(fields=['name'], name='indicator_type_name_idx'),
        ),
        migrations.AddConstraint(
            model_name='indicatortype',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_indicator_type_name'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='indicator_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='indicators', to='indicators.indicatortype', verbose_name='Indicator Type'),
        ),
        migrations.AddIndex(
            model_name='indicatorgeography',
            index=models.Index(fields=['geography'], name='indicator_geography_idx'),
        ),
        migrations.AddConstraint(
            model_name='indicatorgeography',
            constraint=models.UniqueConstraint(fields=('geography', 'indicator'), name='unique_indicator_geography'),
        ),
        migrations.AddIndex(
            model_name='indicator',
            index=models.Index(fields=['name'], name='indicator_name_idx'),
        ),
        migrations.AddConstraint(
            model_name='indicator',
            constraint=models.UniqueConstraint(fields=('name', 'source'), name='unique_indicator_name'),
        ),
        migrations.AddConstraint(
            model_name='indicator',
            constraint=models.UniqueConstraint(fields=('name', 'indicator_set'), name='unique_indicator_indicator_set_name'),
        ),
    ]
