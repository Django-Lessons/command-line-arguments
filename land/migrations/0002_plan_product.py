# Generated by Django 3.0.4 on 2020-05-08 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('cycle', models.CharField(choices=[('m', 'Monthly'), ('a', 'Annual'), ('o', 'One Time')], max_length=24)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
