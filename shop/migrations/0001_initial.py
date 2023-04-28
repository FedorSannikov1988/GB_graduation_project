# Generated by Django 3.2.12 on 2023-04-28 13:01

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DevelopmentTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(blank=True, max_length=20, null=True)),
                ('patronymic', models.CharField(blank=True, max_length=20, null=True)),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True)),
                ('mail', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('role', models.TextField(blank=True, max_length=200, null=True)),
                ('description_work', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_development_team')),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_software_category')),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_software')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.softwarecategory')),
            ],
        ),
        migrations.CreateModel(
            name='FeaturesSoftware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('operating_system', models.CharField(blank=True, max_length=50, null=True)),
                ('video_card', models.TextField(blank=True, max_length=1000, null=True)),
                ('hard_disk_mb', models.PositiveIntegerField(blank=True, null=True)),
                ('min_ram_mb', models.PositiveIntegerField(blank=True, null=True)),
                ('software', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.software')),
            ],
        ),
    ]
