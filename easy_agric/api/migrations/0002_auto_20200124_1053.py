# Generated by Django 3.0.2 on 2020-01-24 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistrictDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=60)),
                ('number', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='District',
        ),
    ]