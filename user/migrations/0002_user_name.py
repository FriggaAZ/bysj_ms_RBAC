# Generated by Django 3.0.4 on 2020-03-22 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='张三', max_length=30, verbose_name='真实姓名'),
            preserve_default=False,
        ),
    ]
