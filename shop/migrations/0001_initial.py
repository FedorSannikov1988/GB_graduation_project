# Generated by Django 3.2.12 on 2023-04-21 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoftwareCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, unique=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_software_сategory')),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareSubcategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, unique=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_software_subcategories')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.softwarecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, unique=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('number_licenses', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_software')),
                ('subcategories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.softwaresubcategories')),
            ],
        ),
    ]
