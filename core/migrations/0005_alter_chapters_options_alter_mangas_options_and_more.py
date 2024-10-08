# Generated by Django 5.1 on 2024-08-14 06:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_mangas_options_mangas_created_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapters',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='mangas',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='chapters',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='chapters',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
