# Generated by Django 2.1 on 2018-07-30 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='warlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warstartT', models.CharField(max_length=50)),
                ('warmsg', models.CharField(max_length=30)),
                ('ctime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
