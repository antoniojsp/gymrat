# Generated by Django 4.1.7 on 2023-03-12 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weight', models.IntegerField(default=0)),
                ('sets', models.IntegerField(default=0)),
                ('reps', models.IntegerField(default=0)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.date')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]