# Generated by Django 3.2.8 on 2021-10-16 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restfull', '0002_comen'),
    ]

    operations = [
        migrations.DeleteModel(
            name='comen',
        ),
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='deskripsi',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='penulis',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
