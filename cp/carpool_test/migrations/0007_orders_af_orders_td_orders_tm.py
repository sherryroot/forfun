# Generated by Django 2.2.1 on 2019-06-29 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carpool_test', '0006_auto_20190629_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders_af',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Tel', models.CharField(max_length=11)),
                ('Addr', models.CharField(max_length=30)),
                ('Time', models.CharField(max_length=10)),
                ('Post', models.CharField(max_length=30)),
                ('Dir', models.CharField(max_length=30)),
            ],
            options={
                'db_table': '后天',
            },
        ),
        migrations.CreateModel(
            name='Orders_td',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Tel', models.CharField(max_length=11)),
                ('Addr', models.CharField(max_length=30)),
                ('Time', models.CharField(max_length=10)),
                ('Post', models.CharField(max_length=30)),
                ('Dir', models.CharField(max_length=5)),
            ],
            options={
                'db_table': '今天',
            },
        ),
        migrations.CreateModel(
            name='Orders_tm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Tel', models.CharField(max_length=11)),
                ('Addr', models.CharField(max_length=30)),
                ('Time', models.CharField(max_length=10)),
                ('Post', models.CharField(max_length=30)),
                ('Dir', models.CharField(max_length=30)),
            ],
            options={
                'db_table': '明天',
            },
        ),
    ]
