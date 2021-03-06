# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-10-27 11:34


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcd', '0010_brand_use_gcdlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatornamedetail',
            name='sort_name',
            field=models.CharField(db_index=True, default='', max_length=255),
        ),
        migrations.AlterModelOptions(
            name='creatornamedetail',
            options={'ordering': ['type__id', 'sort_name', '-id'], 'verbose_name_plural': 'CreatorName Details'},
        ),
        migrations.AddField(
            model_name='creator',
            name='sort_name',
            field=models.CharField(db_index=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='series',
            name='issue_count',
            field=models.IntegerField(default=0),
        ),
    ]
