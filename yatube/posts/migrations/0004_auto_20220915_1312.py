# Generated by Django 2.2.16 on 2022-09-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220914_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='title',
            field=models.CharField(default='Заголовок', max_length=1000, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='Заголовок', max_length=1000, verbose_name='Название'),
        ),
    ]