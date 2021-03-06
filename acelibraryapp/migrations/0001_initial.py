# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 10:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AceMembers',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('oauth_uid', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('api', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=50)),
                ('pic_square', models.CharField(max_length=255)),
                ('course', models.CharField(max_length=10, null=True)),
                ('semester', models.CharField(max_length=10, null=True)),
                ('section', models.CharField(max_length=2, null=True)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('valid', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('ID', models.TextField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.TextField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=30)),
                ('couse_diff', models.CharField(max_length=10)),
                ('couse_des', models.TextField(max_length=50)),
                ('link', models.CharField(max_length=50)),
                ('course_type', models.CharField(max_length=20)),
                ('course_author', models.CharField(max_length=30)),
                ('approval_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('enroll_number', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('email_id', models.EmailField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('approval_status', models.BooleanField(default=False)),
                ('solution', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateTimeField(null=True)),
                ('ifACE', models.BooleanField()),
                ('ifCore', models.BooleanField()),
                ('domain', models.CharField(choices=[('a', 'Programming'), ('b', 'Web Development'), ('c', 'Graphic Desgning'), ('d', 'A/V Editing'), ('e', 'Other')], max_length=1)),
                ('enroll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acelibraryapp.Student')),
            ],
        ),
    ]
