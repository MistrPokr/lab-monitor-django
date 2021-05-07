# Generated by Django 3.2 on 2021-05-07 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VoiceFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('voice_file', models.FileField(upload_to='documents/')),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
