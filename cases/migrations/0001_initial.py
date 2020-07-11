# Generated by Django 3.0.7 on 2020-07-03 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disctrict',
            fields=[
                ('name', models.CharField(max_length=15)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('hosptals', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=1)),
                ('dis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cases.Disctrict')),
            ],
        ),
    ]
