# Generated by Django 4.2.7 on 2023-12-13 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0012_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
