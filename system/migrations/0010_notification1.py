# Generated by Django 5.0.3 on 2024-04-19 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0009_attendence'),
    ]

    operations = [
        migrations.CreateModel(
            name='notification1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tchrname', models.CharField(max_length=100)),
                ('stdname', models.CharField(max_length=100)),
                ('stdemail', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('Area', models.CharField(max_length=100)),
                ('tcrname', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('pay', models.IntegerField()),
            ],
        ),
    ]
