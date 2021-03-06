# Generated by Django 2.2 on 2020-05-10 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20200510_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloggonderi',
            name='eposta',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='bloggonderi',
            name='yazar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
