# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-10-27 11:32


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcd', '0010_brand_use_gcdlink'),
        ('oi', '0010_remove_creatorrevision_data_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviewBrand',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('gcd.brand',),
        ),
        migrations.CreateModel(
            name='PreviewCreator',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('gcd.creator',),
        ),
        migrations.CreateModel(
            name='PreviewCreatorArtInfluence',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('gcd.creatorartinfluence',),
        ),
        migrations.CreateModel(
            name='PreviewCreatorAward',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('gcd.creatoraward',),
        ),
        migrations.CreateModel(
            name='PreviewCreatorDegree',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('gcd.creatordegree',),
        ),
        migrations.CreateModel(
            name='PreviewCreatorMembership',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('gcd.creatormembership',),
        ),
        migrations.CreateModel(
            name='PreviewCreatorNonComicWork',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('gcd.creatornoncomicwork',),
        ),
        migrations.CreateModel(
            name='PreviewCreatorSchool',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('gcd.creatorschool',),
        ),
        migrations.CreateModel(
            name='PreviewIssue',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('gcd.issue',),
        ),
        migrations.CreateModel(
            name='PreviewStory',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('gcd.story',),
        ),
        migrations.RenameField(
            model_name='creatornamedetailrevision',
            old_name='creator',
            new_name='creator_revision',
        ),
        migrations.AlterField(
            model_name='creatorrevision',
            name='bio',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='creatorrevision',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='creatorrevision',
            name='whos_who',
            field=models.URLField(blank=True, default=''),
        ),
    ]
