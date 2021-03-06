# Generated by Django 2.2.11 on 2020-06-26 21:40

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0043_facility_claim_parent_company_verbose_name_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='ppe_contact_email',
            field=models.EmailField(blank=True, help_text='The contact email for PPE-related discussion', max_length=254, null=True, verbose_name='ppe contact email'),
        ),
        migrations.AddField(
            model_name='facility',
            name='ppe_contact_phone',
            field=models.CharField(blank=True, help_text='The contact phone number for PPE-related discussion', max_length=20, null=True, verbose_name='ppe contact phone'),
        ),
        migrations.AddField(
            model_name='facility',
            name='ppe_product_types',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(help_text='A type of personal protective equipment produced at the facility', max_length=50, verbose_name='ppe product type'), blank=True, help_text='The types of personal protective equipment produced at the facility', null=True, size=None, verbose_name='ppe product types'),
        ),
        migrations.AddField(
            model_name='facility',
            name='ppe_website',
            field=models.URLField(blank=True, help_text='The website for PPE information', null=True, verbose_name='ppe website'),
        ),
        migrations.AddField(
            model_name='facilitylistitem',
            name='ppe_contact_email',
            field=models.EmailField(blank=True, help_text='The contact email for PPE-related discussion', max_length=254, null=True, verbose_name='ppe contact email'),
        ),
        migrations.AddField(
            model_name='facilitylistitem',
            name='ppe_contact_phone',
            field=models.CharField(blank=True, help_text='The contact phone number for PPE-related discussion', max_length=20, null=True, verbose_name='ppe contact phone'),
        ),
        migrations.AddField(
            model_name='facilitylistitem',
            name='ppe_product_types',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(help_text='A type of personal protective equipment produced at the facility', max_length=50, verbose_name='ppe product type'), blank=True, help_text='The types of personal protective equipment produced at the facility', null=True, size=None, verbose_name='ppe product types'),
        ),
        migrations.AddField(
            model_name='facilitylistitem',
            name='ppe_website',
            field=models.URLField(blank=True, help_text='The website for PPE information', null=True, verbose_name='ppe website'),
        ),
        migrations.AddField(
            model_name='historicalfacility',
            name='ppe_contact_email',
            field=models.EmailField(blank=True, help_text='The contact email for PPE-related discussion', max_length=254, null=True, verbose_name='ppe contact email'),
        ),
        migrations.AddField(
            model_name='historicalfacility',
            name='ppe_contact_phone',
            field=models.CharField(blank=True, help_text='The contact phone number for PPE-related discussion', max_length=20, null=True, verbose_name='ppe contact phone'),
        ),
        migrations.AddField(
            model_name='historicalfacility',
            name='ppe_product_types',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(help_text='A type of personal protective equipment produced at the facility', max_length=50, verbose_name='ppe product type'), blank=True, help_text='The types of personal protective equipment produced at the facility', null=True, size=None, verbose_name='ppe product types'),
        ),
        migrations.AddField(
            model_name='historicalfacility',
            name='ppe_website',
            field=models.URLField(blank=True, help_text='The website for PPE information', null=True, verbose_name='ppe website'),
        ),
    ]
