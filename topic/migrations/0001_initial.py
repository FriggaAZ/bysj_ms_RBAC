# Generated by Django 3.0.4 on 2020-03-21 07:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='题目')),
                ('detail', models.TextField(verbose_name='描述')),
                ('chosen_num', models.SmallIntegerField(verbose_name='已选人数')),
                ('limit_num', models.SmallIntegerField(choices=[(1, '限1人'), (2, '限2人'), (3, '限3人')], verbose_name='限选人数')),
                ('release_time', models.DateTimeField(verbose_name='出题时间')),
                ('status', models.SmallIntegerField(choices=[(1, '未选'), (2, '已选')], default=1, verbose_name='选题状态')),
                ('accept', models.SmallIntegerField(choices=[(1, '未选'), (2, '已选')], default=0, verbose_name='确认状态')),
            ],
        ),
        migrations.CreateModel(
            name='Topic2User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topic.TopicRecord')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]