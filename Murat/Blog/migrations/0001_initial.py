# Generated by Django 2.2 on 2020-05-09 09:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogGonderi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=200)),
                ('yazi', models.TextField()),
                ('olusturma_zamani', models.DateTimeField(default=django.utils.timezone.now)),
                ('yayim_zamani', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
