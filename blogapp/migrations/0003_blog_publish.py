# Generated by Django 4.0.2 on 2023-01-24 03:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_blog_options_remove_blog_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='publish',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]