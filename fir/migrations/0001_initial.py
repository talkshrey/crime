# Generated by Django 4.0.3 on 2022-03-14 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Helpline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Emergency', max_length=20)),
                ('number', models.BigIntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('vote', models.PositiveIntegerField(blank=True, default=0, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number', models.BigIntegerField(blank=True)),
                ('address', models.TextField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('crime_type', models.CharField(choices=[('Dacoity', 'Dacoity'), ('Robbery', 'Robbery'), ('Rape', 'Rape')], max_length=50)),
                ('desc', models.TextField(blank=True, max_length=255, null=True)),
                ('proof', models.FileField(blank=True, upload_to='')),
                ('option', models.BooleanField()),
                ('votes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fir.vote')),
            ],
        ),
    ]
