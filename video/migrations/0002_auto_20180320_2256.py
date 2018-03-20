# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-20 14:56
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import video.models
import videokit.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='分类名')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '分类',
                'ordering': ['name'],
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(1)])),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '点赞',
                'verbose_name_plural': '点赞',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('username', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='VideoItem',
            fields=[
                ('video', videokit.models.VideoField(duration_field='video_duration', height_field='video_height', mimetype_field='video_mimetype', rotation_field='video_rotation', thumbnail_field='video_thumbnail', upload_to=video.models.upload_to, width_field='video_width')),
                ('source_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('video_width', models.IntegerField(blank=True, null=True)),
                ('video_height', models.IntegerField(blank=True, null=True)),
                ('video_rotation', models.FloatField(blank=True, null=True)),
                ('video_mimetype', models.CharField(blank=True, max_length=32, null=True)),
                ('video_duration', models.IntegerField(blank=True, null=True)),
                ('video_thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('video_mp4', videokit.models.VideoSpecField(blank=True, null=True, upload_to='')),
                ('video_ogg', videokit.models.VideoSpecField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='视频名称')),
                ('describe', models.TextField(verbose_name='描述')),
                ('upload_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='上传时间')),
                ('pub_time', models.DateTimeField(blank=True, null=True, verbose_name='发布时间')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='观看次数')),
                ('comment_status', models.CharField(choices=[('o', '打开'), ('c', '关闭')], default='o', max_length=1, verbose_name='评论状态')),
                ('status', models.CharField(choices=[('d', '草稿'), ('p', '发表')], default='p', max_length=1, verbose_name='视频状态')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='video.Category', verbose_name='分类')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '视频',
                'ordering': ['-pub_time'],
                'verbose_name_plural': '视频',
                'get_latest_by': 'upload_time',
            },
        ),
        migrations.DeleteModel(
            name='MediaItem',
        ),
        migrations.AddField(
            model_name='rating',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.VideoItem'),
        ),
        migrations.AddField(
            model_name='likes',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.VideoItem', verbose_name='视频'),
        ),
        migrations.AddField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.VideoItem'),
        ),
    ]
