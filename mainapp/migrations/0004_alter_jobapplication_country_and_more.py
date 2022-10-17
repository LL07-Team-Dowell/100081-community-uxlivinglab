# Generated by Django 4.1.1 on 2022-10-10 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_country_city_alter_job_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country', to='mainapp.country'),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobapplication', to='mainapp.job'),
        ),
    ]