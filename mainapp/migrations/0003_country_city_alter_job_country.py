# Generated by Django 4.1.1 on 2022-10-10 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_jobapplication_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job', to='mainapp.country'),
        ),
    ]