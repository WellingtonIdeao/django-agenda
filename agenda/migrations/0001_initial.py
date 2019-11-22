# Generated by Django 2.2.7 on 2019-11-06 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('idade', models.IntegerField()),
                ('sexo', models.CharField(max_length=10)),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
    ]
