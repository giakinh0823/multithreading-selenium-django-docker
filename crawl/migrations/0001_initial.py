# Generated by Django 3.2.6 on 2021-08-08 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=2000)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, max_length=2000, null=True, upload_to='product/products')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crawl.category')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crawl.service')),
                ('size', models.ManyToManyField(to='crawl.Size')),
            ],
        ),
    ]
