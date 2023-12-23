# Generated by Django 4.2.7 on 2023-11-10 17:11

from django.conf import settings
import django.contrib.auth
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('syllabus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluationsystem',
            name='criteria',
        ),
        migrations.RemoveField(
            model_name='evaluationsystem',
            name='weight',
        ),
        migrations.AddField(
            model_name='evaluationsystem',
            name='mp',
            field=models.CharField(max_length=255, null=True, verbose_name='Максимальный процент (%)'),
        ),
        migrations.AddField(
            model_name='evaluationsystem',
            name='mv',
            field=models.CharField(max_length=255, null=True, verbose_name='Максимальный вес (%)'),
        ),
        migrations.AddField(
            model_name='evaluationsystem',
            name='tb',
            field=models.CharField(max_length=255, null=True, verbose_name='Итого в баллах'),
        ),
        migrations.AddField(
            model_name='evaluationsystem',
            name='tm',
            field=models.CharField(max_length=255, null=True, verbose_name='Тема / модуль'),
        ),
        migrations.AddField(
            model_name='evaluationsystem',
            name='vk',
            field=models.CharField(max_length=255, null=True, verbose_name='Всего за курс'),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='user',
            field=models.ForeignKey(default=django.contrib.auth.get_user_model, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='evaluationsystem',
            name='syllabus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='syllabus.syllabus', verbose_name='Силлабус'),
        ),
        migrations.AlterField(
            model_name='philosophyandpolicy',
            name='philosophy',
            field=models.TextField(verbose_name='Философия преподавания и обучения'),
        ),
    ]