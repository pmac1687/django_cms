# Generated by Django 3.1.7 on 2021-03-22 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('tag', models.CharField(default='', help_text='format: #word , #word_2; seperate by comma', max_length=200)),
                ('color', models.CharField(default='red', help_text='format: ex. blue', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MarketSegments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('svg', models.FileField(default='', upload_to='uploads')),
            ],
        ),
    ]
