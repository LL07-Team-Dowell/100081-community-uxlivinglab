# Generated by Django 4.1 on 2022-10-17 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_catagaries_form_jobcatagaries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcatagaries',
            name='is_active',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
