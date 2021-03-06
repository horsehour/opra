# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-28 20:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0058_auto_20160728_1647'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('multipolls', '0004_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Combination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dependencies', models.ManyToManyField(to='polls.Item')),
                ('dependent_questions', models.ManyToManyField(related_name='dependent_questions', to='polls.Question')),
                ('response', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Response')),
                ('target_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ConditionalItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('combination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multipolls.Combination')),
                ('items', models.ManyToManyField(to='polls.Item')),
                ('response', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Response')),
            ],
        ),
    ]
