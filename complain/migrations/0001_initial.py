# Generated by Django 3.1.4 on 2021-01-01 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactcomplain',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('query_status', models.CharField(default='Pending', max_length=5000)),
                ('querytype', models.CharField(default='', max_length=5000)),
                ('querydesc', models.CharField(default='', max_length=5000)),
                ('querysub', models.CharField(default='', max_length=5000)),
                ('name', models.CharField(default='', max_length=90)),
                ('email', models.CharField(default='', max_length=111)),
                ('phone', models.CharField(default='', max_length=111)),
                ('rollnumber', models.CharField(default='', max_length=111)),
                ('branchyear', models.CharField(default='', max_length=111)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contactenquiry',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('query_status', models.CharField(default='', max_length=5000)),
                ('querytype', models.CharField(default='', max_length=5000)),
                ('querydesc', models.CharField(default='', max_length=5000)),
                ('querysub', models.CharField(default='', max_length=5000)),
                ('name', models.CharField(default='', max_length=90)),
                ('email', models.CharField(default='', max_length=111)),
                ('phone', models.CharField(default='', max_length=111)),
                ('rollnumber', models.CharField(default='', max_length=111)),
                ('branchyear', models.CharField(default='', max_length=111)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
