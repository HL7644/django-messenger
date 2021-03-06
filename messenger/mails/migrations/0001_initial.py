# Generated by Django 2.1.1 on 2022-07-13 14:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.CharField(max_length=100)),
                ('to_user', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
