# Generated by Django 5.2.3 on 2025-07-09 16:21

import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manhwas', '0008_alter_episode_manhwa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='manhwa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='episodes', to='manhwas.manhwa', verbose_name='قسمت ها'),
        ),
        migrations.AlterField(
            model_name='manhwa',
            name='summary',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
    ]
