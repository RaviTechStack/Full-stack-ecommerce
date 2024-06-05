# Generated by Django 4.1.5 on 2023-05-06 07:39

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='allproducts',
            fields=[
                ('prod_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_name', models.CharField(max_length=50)),
                ('prod_desc', models.CharField(max_length=500)),
                ('prod_category', models.CharField(max_length=50)),
                ('prod_sub_category', models.CharField(max_length=50)),
                ('prod_price', models.IntegerField()),
                ('prod_orig_price', models.IntegerField()),
                ('prod_slug', autoslug.fields.AutoSlugField(editable=False, populate_from=models.CharField(max_length=50), unique=True)),
                ('prod_view', models.IntegerField()),
            ],
        ),
    ]
