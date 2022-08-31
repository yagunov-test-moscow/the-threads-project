# Generated by Django 2.2.16 on 2022-08-31 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20220821_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='difficulty',
            field=models.ForeignKey(blank=True, help_text='Укажите уровень сложности', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.Difficulty', verbose_name='Сложность вопроса'),
        ),
    ]