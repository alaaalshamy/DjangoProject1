# Generated by Django 2.0.1 on 2018-03-07 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_publish', models.DateTimeField(default='')),
                ('sammary', models.TextField(blank=True)),
                ('country', models.TextField(blank=True)),
                ('link', models.URLField(blank=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('witer_name', models.CharField(max_length=200)),
                ('date_birth', models.DateTimeField(default='')),
                ('date_death', models.DateTimeField(default='')),
                ('Contact', models.URLField(blank=True)),
                ('Bio', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='Writer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='liberary.Writer'),
        ),
    ]