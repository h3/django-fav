# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-19 13:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_object_id', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('target_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
                'verbose_name_plural': 'favorites',
                'get_latest_by': 'timestamp',
                'verbose_name': 'favorite',
            },
        ),
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together=set([('user', 'target_content_type', 'target_object_id')]),
        ),
    ]
